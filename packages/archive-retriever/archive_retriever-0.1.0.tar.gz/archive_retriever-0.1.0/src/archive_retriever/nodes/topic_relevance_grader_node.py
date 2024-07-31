import concurrent.futures
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
from archive_retriever.state.topic_state import TopicState


def generate_topic_relevance_grader_llm_data_model_class(article_count):
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
    return type("TopicRelevanceGraderLlmDataModel", (BaseModel,), fields)


def topic_relevance_grader_node(agent_state: AgentState):
    prompt_template_string = """
    Generell:
    - Du bist der "Topic-Relevance-Grader"-Mitarbeiter bei der Nordseezeitung in Bremerhaven.
    - Du und deine Kollegen seit für das Archiv zuständig.
    - Das Archiv ist eine Vektordatenbank, welche alle Zeitungsartikel, die die Zeitung jemals veröffentlicht hat, enthält. Die Zeitungsartikel wurden durch ein Embeddingmodel embedded.
    - Ein menschlicher Mitarbeiter kommt zu euch mit einer Nutzeranfrage/Frage, dessen Antworten sich im Archiv verstecken und ihr müsst die Frage so gut wie möglich beantworten.

    Ablauf:
    - Du bekommst vom "Topic-Retriever"-Mitarbeiter einige Zeitungsartikel aus dem Archiv, welche er relevant für die Nutzeranfrage hält.
    - Deine Aufgabe ist es, jeden der Zeitungsartikel zu bewerten, ob diese relevant für die Beantwortung der Nutzeranfrage sind oder nicht.
    - Behandle die Artikel von einander komplett unabhängig.
    - Sei dabei nicht zu streng, Artikel können auch nur teilweise relevant sein, oder entfernt über eine Verbindung relevant sein.
    - Wenn es also schon nur sehr sehr weit entfernt um das richtige Thema oder die richtigen Leute, Objekte, Gebäude oder Orte etc. geht, ist der Artikel relevant.
    - Deine Antwort hat zwei Auswirkungen. Zum einen werden Artikel, die du als irrelevant kennzeichnest, nicht zur Beantwortung der Nutzeranfrage zu Rate gezogen.
    - Des Weiteren wird dein Feedback an den "Retriever"-Mitarbeiter zurückgegeben, sodass dieser nochmal versuchen kann, relevantere Artikel aus dem Archiv zu holen.

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

    <Zeitungsartikel>
    {articles_xml}
    </Zeitungsartikel>
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template_string)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.25)
    TopicRelevanceGraderLlmDataModel = (
        generate_topic_relevance_grader_llm_data_model_class(
            agent_state["quality_config"]["topic_top_k"]
        )
    )
    structured_llm = llm.with_structured_output(TopicRelevanceGraderLlmDataModel)
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

    def process_topic(topic, chain, query):
        if topic["state"] != TopicState.CLEANED:
            return topic

        unique_articles = [
            article for article in topic["articles"] if not article["is_doubled"]
        ]
        response = chain.invoke(
            {
                "query": query,
                "articles": unique_articles,
            }
        )
        for unique_article_index, unique_article in enumerate(unique_articles):
            for article in topic["articles"]:
                if article["id"] == unique_article["id"]:
                    article["is_relevant"] = getattr(
                        response, f"is_article_{unique_article_index+1}_relevant"
                    )
                    article["feedback"] = getattr(
                        response, f"article_{unique_article_index+1}_feedback"
                    )
                    article["state"] = ArticleState.GRADED
                    break
        return topic

    query = agent_state["query"]
    with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
        process_topic_partial = partial(process_topic, chain=chain, query=query)
        updated_topics = list(
            thread_pool_executor.map(process_topic_partial, agent_state["topics"])
        )
    agent_state["topics"] = updated_topics
    # Repair duplicated articles
    for topic in agent_state["topics"]:
        for article in topic["articles"]:
            if not article["is_doubled"]:
                continue
            unique_article = next(
                (
                    article2
                    for topic2 in agent_state["topics"]
                    for article2 in topic2["articles"]
                    if article["unique_article_id"] == article2["id"]
                ),
                None,
            )
            if unique_article:
                article["is_relevant"] = unique_article["is_relevant"]
                article["feedback"] = unique_article["feedback"]
                article["state"] = ArticleState.GRADED
    # Process topic relevance
    for topic in agent_state["topics"]:
        topic["is_relevant"] = (
            len([article for article in topic["articles"] if article["is_relevant"]])
            >= agent_state["quality_config"][
                "min_relevant_article_count_for_relevant_topic"
            ]
        )
        if topic["is_relevant"]:
            topic["feedback"] = ""
        else:
            topic["feedback"] = "\n".join(
                [
                    f"Artikel {i+1}: {article['feedback']}"
                    for i, article in enumerate(topic["articles"])
                    if not article["is_relevant"]
                ]
            )
        topic["state"] = TopicState.GRADED

    return agent_state
