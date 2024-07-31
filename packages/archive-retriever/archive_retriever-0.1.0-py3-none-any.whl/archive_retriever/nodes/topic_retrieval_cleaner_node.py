from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article import (
    check_are_articles_equal,
    sort_articles_by_date,
)
from archive_retriever.state.topic_state import TopicState
from archive_retriever.utilities.get_article_text import (
    get_article_text,
)


def topic_retrieval_cleaner_node(agent_state: AgentState):
    agent_state["topics"] = sorted(
        agent_state["topics"], key=lambda topic: len(topic["articles"]), reverse=True
    )
    unique_articles = []
    for topic in agent_state["topics"]:
        if topic["state"] != TopicState.RETRIEVED:
            continue
        topic["articles"] = sort_articles_by_date(topic["articles"])
        for article in topic["articles"]:
            article["text"] = get_article_text(article)
            existing_unique_article = next(
                (
                    unique_article
                    for unique_article in unique_articles
                    if check_are_articles_equal(article, unique_article)
                ),
                None,
            )
            if existing_unique_article:
                article["is_doubled"] = True
                article["unique_article_id"] = existing_unique_article["id"]
            else:
                unique_articles.append(article)
                article["is_doubled"] = False
        topic["state"] = TopicState.CLEANED
    return agent_state
