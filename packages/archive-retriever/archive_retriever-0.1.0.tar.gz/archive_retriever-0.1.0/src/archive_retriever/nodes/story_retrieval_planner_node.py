import concurrent.futures
import uuid
from datetime import datetime
from functools import partial
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article import (
    format_article_to_text,
    get_datetime_of_article,
)
from archive_retriever.state.story_state import StoryState


class StoryRetrievalPlannerLlmDataModel(BaseModel):
    is_potential_story: bool = Field(
        description="Ist der Artikel ein potenzieller Teil einer Storyline?"
    )
    title: str = Field(description="Der Titel der Storyline")
    summary: str = Field(description="Die Zusammenfassung der Storyline")


def story_retrieval_planner_node(agent_state: AgentState):
    # TODO Bulk processing of articles in one llm call
    prompt_template_string = """
    Generell:
    - Du bist der "Story-Retrieval-Planner"-Mitarbeiter bei der Nordseezeitung in Bremerhaven.
    - Du und deine Kollegen seit für das Archiv zuständig.
    - Das Archiv ist eine Vektordatenbank, welche alle Zeitungsartikel, die die Zeitung jemals veröffentlicht hat, enthält. Die Zeitungsartikel wurden durch ein Embeddingmodel embedded.
    - Ein menschlicher Mitarbeiter kommt zu euch mit einer Nutzeranfrage/Frage, dessen Antworten sich im Archiv verstecken und ihr müsst die Frage so gut wie möglich beantworten.

    Ablauf:
    - Du bekommst vom "Topic-Retriever"-Mitarbeiter die Zeitungsartikel aus dem Archiv, welche er für relevant zur Beantwortung der Nutzeranfrage hält.
    - Deine Aufgabe ist es, zu prüfen, ob es sich bei dem Zeitungsartikel potentiel um einen Teil einer Storyline handelt, also um einen Teil einer Serie von Artikeln in einem bestimmten Zeitraum zu dem selben Thema.
    - Wenn ja, schreibe einen sehr kurzen Titel und eine genaue Zusammenfassung des Artikels.
    - Deine Antwort geht an den "Retriever"-Mitarbeiter, welcher dann versuche, weitere Artikel der Story zu finden.
    - Dies tut er, indem er das die Vektordatenbank mit einer Similarity-Search auf die Zusammenfassung des Artikels und einem Filter auf den Zeitraum der Storyline durchsucht.

    Beispiele:
    - Eine Todesanzeige ist kein Teil einer Storyline.
    - Ein Artikel zu Hochwasser könnte ein Teil einer Storyline sein, da die Zeitung über dieses wahrscheinlich mehrmals berichten wird.
    - Ein Artikel zur aktuellen Arbeitslosen-Situation könnte Teil einer Geschichte sein, welche aktuell von den Medien beachtet wird und zur aktuellen Zeit immer mal wieder einen Artikel hervorbringt, da es einfach ein aktuelles Thema ist.

    
    Aktuelles Datum und Uhrzeit: {formatted_current_datetime}

    
    Zeitungsartikel, welchen du verarbeiten sollst:

    <Zeitungsartikel>
    {article}
    </Zeitungsartikel>
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template_string)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.25)
    structured_llm = llm.with_structured_output(StoryRetrievalPlannerLlmDataModel)
    chain = (
        (
            {
                "article": itemgetter("article")
                | RunnableLambda(format_article_to_text),
                "formatted_current_datetime": lambda x: datetime.now().strftime(
                    "%d.%m.%Y %H:%M"
                ),
            }
        )
        | prompt_template
        | structured_llm
    )

    def process_article(article, chain):
        if article["is_doubled"] or not article["is_relevant"]:
            return None
        response = chain.invoke({"article": article})
        if response.is_potential_story and response.title and response.summary:
            return {
                "id": str(uuid.uuid4()),
                "state": StoryState.INITIAL,
                "initial_article": article,
                "date_time": get_datetime_of_article(article),
                "title": response.title,
                "summary": response.summary,
            }
        return None

    stories = []
    with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
        process_article_partial = partial(process_article, chain=chain)
        futures = []
        for topic in agent_state["topics"]:
            for article in topic["articles"]:
                if len(stories) >= agent_state["quality_config"]["story_limit"]:
                    break
                futures.append(
                    thread_pool_executor.submit(process_article_partial, article)
                )
            if len(stories) >= agent_state["quality_config"]["story_limit"]:
                break

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                stories.append(result)
                if len(stories) >= agent_state["quality_config"]["story_limit"]:
                    break
    agent_state["stories"].extend(stories)
    return agent_state
