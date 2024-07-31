import concurrent.futures
import uuid
from datetime import datetime
from functools import partial
from operator import itemgetter
from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article import format_articles_to_inner_xml
from archive_retriever.state.topic_state import TopicState


class SubRetrievalPlannerLlmDataModel(BaseModel):
    topics: List[str] = Field(description="Die Sub-Themenbereiche")


def sub_topic_retrieval_planner_node(agent_state: AgentState):
    # TODO Make sure the newly generated topics are new ones and no doubles with the old ones or so
    prompt_template_string = """
    Generell:
    - Du bist der "Sub-Topic-Retrieval-Planner"-Mitarbeiter bei der Nordseezeitung in Bremerhaven.
    - Du und deine Kollegen seit für das Archiv zuständig.
    - Das Archiv ist eine Vektordatenbank, welche alle Zeitungsartikel, die die Zeitung jemals veröffentlicht hat, enthält. Die Zeitungsartikel wurden durch ein Embeddingmodel embedded.
    - Ein menschlicher Mitarbeiter kommt zu euch mit einer Nutzeranfrage/Frage, dessen Antworten sich im Archiv verstecken und ihr müsst die Frage so gut wie möglich beantworten.

    Ablauf:
    - Du bekommst vom "Topic-Retriever"-Mitarbeiter zehn Zeitungsartikel aus dem Archiv, welche er relevant für die Nutzeranfrage hält.
    - Deine Aufgabe ist es, aus diesen Zeitungsartikeln neue Themenbereiche zu extrahieren, welche der Retriever dann wieder in der Vektordatenbank suchen kann.
    - Die Themenbereiche sollten aber trotzdem noch einen sehr guten Detailgrad haben und ein ganzer Satz sein.
    - Gebe mindestens 1 Themenbereich an und maximal {sub_topic_generation_limit}.
    - Deine Antwort geht an den "Retriever"-Mitarbeiter, welcher dann die Zeitungsartikel mit einer Similarity-Search aus der Vektordatenbank holt.

    Beispiele:
    - Nutzeranfrage 1: "Wie war das Essen im Zweiten Weltkrieg?"
    - Themenbereiche 1: "Essen und Speisen im Zweiten Weltkrieg"

    - Nutzeranfrage 2: "Wie hat sich das Einkaufszentrum entwickelt?"
    - Themenbereiche 2: "Entwicklung des Einkaufszentrums\nEinkaufszentrum Start\nEinkaufszentrum Ende"

    - Nutzeranfrage 3: "Was haben wir über Elvis Presley rausgegeben?"
    - Themenbereiche 3: "Elvis Presley Biografie\nElvis Presley Musik\nElvis Presley Konzerte\nElvis Presley Privatleben\nElvis Presley Tod"

    
    Aktuelles Datum und Uhrzeit: {formatted_current_datetime}


    Nutzeranfrage, welche du verarbeiten sollst:

    <Nutzeranfrage>
    {query}
    </Nutzeranfrage>


    Zeitungsartikel, welche du verarbeiten sollst:

    <Zeitungsartikel>
    {articles_xml}
    </Zeitungsartikel>
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template_string)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.25)
    structured_llm = llm.with_structured_output(SubRetrievalPlannerLlmDataModel)
    chain = (
        {
            "sub_topic_generation_limit": itemgetter("sub_topic_generation_limit"),
            "query": itemgetter("query"),
            "articles_xml": itemgetter("articles")
            | RunnableLambda(format_articles_to_inner_xml),
            "formatted_current_datetime": lambda x: datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            ),
        }
        | prompt_template
        | structured_llm
    )

    def process_topic(topic, chain, sub_topic_generation_limit, query):
        response = chain.invoke(
            {
                "sub_topic_generation_limit": sub_topic_generation_limit,
                "query": query,
                "articles": [
                    article
                    for article in topic["articles"]
                    if not article["is_doubled"]
                ],
            }
        )
        return [
            {
                "id": str(uuid.uuid4()),
                "title": sub_topic,
                "state": TopicState.INITIAL,
            }
            for sub_topic in response.topics
        ]

    most_relevant_topics = sorted(
        agent_state["topics"],
        key=lambda topic: len(
            [
                article
                for article in topic["articles"]
                if not article["is_doubled"] and article["is_relevant"]
            ]
        ),
        reverse=True,
    )[: agent_state["quality_config"]["sub_topic_generation_limit"]]

    sub_topic_generation_limit = agent_state["quality_config"][
        "sub_topic_generation_limit"
    ]
    query = agent_state["query"]

    with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
        process_topic_partial = partial(
            process_topic,
            chain=chain,
            sub_topic_generation_limit=sub_topic_generation_limit,
            query=query,
        )
        new_topics_lists = list(
            thread_pool_executor.map(process_topic_partial, most_relevant_topics)
        )

    new_topics = [topic for sublist in new_topics_lists for topic in sublist]
    agent_state["topics"] += new_topics
    return agent_state
