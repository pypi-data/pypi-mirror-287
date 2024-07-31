import uuid
from datetime import datetime
from operator import itemgetter
from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.topic import format_topics_to_feedback_text
from archive_retriever.state.topic_state import TopicState


class RetrievalPlannerLlmDataModel(BaseModel):
    topic_titles: List[str] = Field(description="Die Themenbereiche")


def topic_retrieval_planner_node(agent_state: AgentState):
    # TODO Beispiele
    prompt_template_string = """
    Generell:
    - Du bist der "Topic-Retrieval-Planner"-Mitarbeiter bei der Nordseezeitung in Bremerhaven.
    - Du und deine Kollegen seit für das Archiv zuständig.
    - Das Archiv ist eine Vektordatenbank, welche alle Zeitungsartikel, die die Zeitung jemals veröffentlicht hat, enthält. Die Zeitungsartikel wurden durch ein Embeddingmodel embedded.
    - Ein menschlicher Mitarbeiter kommt zu euch mit einer Nutzeranfrage/Frage, dessen Antworten sich im Archiv verstecken und ihr müsst die Frage so gut wie möglich beantworten.

    Ablauf:
    - Du bist der erste, der die Nutzeranfrage verarbeitet.
    - Eine Nutzeranfrage kann auf mehrere Themenbereiche abzielen und wenn der Retriever eine Suche mit einem gemischten Themenbereich auf der Vektordatenbank durchführen, bekommen er sehr ungenaue Ergebnisse.
    - Deine Aufgabe ist es, die Nutzeranfrage in spezifischere, genauere, abzielendere Anfragen an die Vektordatenbank zu konvertieren.
    - Die Themenbereiche sollten aber trotzdem noch einen sehr guten Detailgrad haben und ein ganzer Satz sein.
    - Gebe mindestens 1 Themenbereich an und maximal {topic_generation_limit}.
    - Deine Antwort geht an den "Retriever"-Mitarbeiter, welcher dann die Zeitungsartikel mit einer Similarity-Search aus der Vektordatenbank holt.

    - Du wirst für die gleiche Nutzeranfrage mehrmals durchlaufen, damit du mehrere Chancen hast, die perfekten Themenbereiche zu finden.
    - Damit du weißt wie du dich verbessern kannst, wird dir vom "Relevance-Grader"-Mitarbeiter Feedback gegeben, ob die Themenbereiche, die du vorgeschlagen hast, relevant Artikel hervorgebracht haben oder nicht.
    - Wenn du Feedback bekommst, versuche nochmal für jeden irrelevanten Themenbereich einen KOMPLETT NEUEN Themenbereich zu finden.

    
    Aktuelles Datum und Uhrzeit: {formatted_current_datetime}


    Nutzeranfrage, welche du verarbeiten sollst:

    <Nutzeranfrage>
    {query}
    </Nutzeranfrage>


    Feedback, welches du vom "Relevance-Grader"-Mitarbeiter bekommen hast:

    <Feedback>
    {feedback}
    </Feedback>
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template_string)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.25)
    structured_llm = llm.with_structured_output(RetrievalPlannerLlmDataModel)
    chain = (
        {
            "topic_generation_limit": itemgetter("topic_generation_limit"),
            "query": itemgetter("query"),
            "feedback": itemgetter("topics")
            | RunnableLambda(format_topics_to_feedback_text),
            "formatted_current_datetime": lambda x: datetime.now().strftime(
                "%d.%m.%Y %H:%M"
            ),
        }
        | prompt_template
        | structured_llm
    )
    print(agent_state)
    response = chain.invoke(
        {
            "topic_generation_limit": agent_state["quality_config"][
                "topic_generation_limit"
            ],
            "query": agent_state["query"],
            "topics": agent_state["topics"],
        }
    )
    agent_state["topics"] += [
        {"id": str(uuid.uuid4()), "state": TopicState.INITIAL, "title": topic_title}
        for topic_title in response.topic_titles
    ]
    agent_state["topics"] = agent_state["topics"][
        : agent_state["quality_config"]["topic_limit"]
    ]
    return agent_state
