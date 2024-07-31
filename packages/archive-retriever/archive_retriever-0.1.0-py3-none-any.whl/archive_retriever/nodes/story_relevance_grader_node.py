import concurrent.futures
import re
import uuid
from datetime import datetime
from functools import partial
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article import format_articles_to_inner_xml
from archive_retriever.state.article_state import ArticleState
from archive_retriever.state.story_state import StoryState


def generate_story_relevance_grader_llm_data_model_class(
    type_name_postfix, article_count
):
    fields = {}
    for i in range(1, article_count + 1):
        relevance_field_name = f"is_article_{i}_relevant"
        feedback_field_name = f"article_{i}_feedback"
        fields[relevance_field_name] = Field(
            default=False, description=f"Is the {i}. article relevant?"
        )
        fields[feedback_field_name] = Field(
            default="",
            description=f"Very short and feedback for the retriever on why the {i}. article is relevant or not.",
        )
    return type(
        # "StoryRelevanceGraderLlmDataModel" + type_name_postfix, (BaseModel,), fields
        "SRGLDM" + type_name_postfix,
        (BaseModel,),
        fields,
    )


def story_relevance_grader_node(agent_state: AgentState):
    prompt_template_string = """ 
    Generell:
    - Du bist der "Story-Relevance-Grader"-Mitarbeiter bei der Nordseezeitung in Bremerhaven.
    - Du und deine Kollegen seit für das Archiv zuständig.
    - Das Archiv ist eine Vektordatenbank, welche alle Zeitungsartikel, die die Zeitung jemals veröffentlicht hat, enthält. Die Zeitungsartikel wurden durch ein Embeddingmodel embedded.
    - Ein menschlicher Mitarbeiter kommt zu euch mit einer Nutzeranfrage/Frage, dessen Antworten sich im Archiv verstecken und ihr müsst die Frage so gut wie möglich beantworten.

    Ablauf:
    - Du bekommst vom "Story-Retriever"-Mitarbeiter einige Zeitungsartikel aus dem Archiv, welche er relevant für die Nutzeranfrage hält.
    - Deine Aufgabe ist es, jeden der Zeitungsartikel zu bewerten, ob diese relevant für die Beantwortung der Nutzeranfrage sind oder nicht.
    - Behandle die Artikel von einander komplett unabhängig.
    - Sei dabei nicht zu streng, Artikel können auch nur teilweise relevant sein, oder entfernt über eine Verbindung relevant sein.
    - Wenn es also schon nur sehr sehr weit entfernt um das richtige Thema oder die richtigen Leute, Objekte, Gebäude oder Orte etc. geht, ist der Artikel relevant.
    - Artikel, welche du als irrelevant kennzeichnest, nicht zur Beantwortung der Nutzeranfrage zu Rate gezogen.

    Beispiele:
    - Nutzeranfrage 1: "Wie war das Essen im Zweiten Weltkrieg?"
    - Zeitungsartikel 1: "Max Mustermann ist leider verstorben..."
    - Antwort 1: "False" und "Irrelevant, da dies eine Todesanzeige ist und nichts mit dem Essen im zweiten Weltkrieg zu tun hat."

    - Nutzeranfrage 2: "Wie hat sich das Einkaufszentrum entwickelt?"
    - Zeitungsartikel 2: "Kaufen Sie jetzt den neuen Staubsauger-X1000..."
    - Antwort 1: "False" und "Irrelevant, da dies eine Werbung ist und nichts mit der Entwicklung des Einkaufszentrums zu tun hat."

    - Nutzeranfrage 3: "Was haben wir über Elvis Presley rausgegeben?"
    - Zeitungsartikel 3: "Elvis Presley war ein großartiger Musiker...."
    - Antwort 3: "True" und "Relevant"


    Aktuelles Datum und Uhrzeit: {formatted_current_datetime}


    Nutzeranfrage, welche du verarbeiten sollst:

    <Nutzeranfrage>
    {query}
    </Nutzeranfrage>


    Zeitungsartikel, welche du verarbeiten sollst:

    {articles_xml}
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template_string)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.25)

    def process_story(story, query, prompt_template, llm):
        if story["state"] != StoryState.CLEANED:
            return story
        LlmDataModel = generate_story_relevance_grader_llm_data_model_class(
            re.sub("[^a-zA-Z]", "", str(uuid.uuid4())), len(story["articles"])
        )
        structured_llm = llm.with_structured_output(LlmDataModel)
        chain = (
            {
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
        unique_articles = [
            article for article in story["articles"] if not article["is_doubled"]
        ]
        response = chain.invoke(
            {
                "query": query,
                "articles": unique_articles,
            }
        )
        for unique_article_index, unique_article in enumerate(unique_articles):
            for article in story["articles"]:
                if article["id"] == unique_article["id"]:
                    article["is_relevant"] = getattr(
                        response, f"is_article_{unique_article_index+1}_relevant"
                    )
                    article["feedback"] = getattr(
                        response, f"article_{unique_article_index+1}_feedback"
                    )
                    article["state"] = ArticleState.GRADED
                    break
        story["state"] = StoryState.GRADED
        return story

    query = agent_state["query"]
    with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
        process_story_partial = partial(
            process_story,
            query=query,
            prompt_template=prompt_template,
            llm=llm,
        )
        updated_stories = list(
            thread_pool_executor.map(process_story_partial, agent_state["stories"])
        )

    agent_state["stories"] = updated_stories

    # Repair duplicated articles
    for story in agent_state["stories"]:
        for article in story["articles"]:
            if not article["is_doubled"]:
                continue
            unique_article = next(
                (
                    article2
                    for story2 in agent_state["stories"]
                    for article2 in story2["articles"]
                    if article["unique_article_id"] == article2["id"]
                ),
                None,
            )
            if unique_article:
                article["is_relevant"] = unique_article["is_relevant"]
                article["feedback"] = unique_article["feedback"]
                article["state"] = ArticleState.GRADED

    return agent_state
