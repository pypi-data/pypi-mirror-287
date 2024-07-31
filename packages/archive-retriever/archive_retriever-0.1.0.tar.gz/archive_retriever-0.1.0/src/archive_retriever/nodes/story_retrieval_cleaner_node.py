from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article import (
    check_are_articles_equal,
    sort_articles_by_date,
)
from archive_retriever.state.story_state import StoryState
from archive_retriever.utilities.get_article_text import (
    get_article_text,
)


def story_retrieval_cleaner_node(agent_state: AgentState):
    # TODO Maybe summarize each article, or maybe this summarization should be done on upserting the docs? this summarization could also be embedded as a second vector in the pinecone index
    agent_state["stories"] = sorted(
        agent_state["stories"], key=lambda story: len(story["articles"]), reverse=True
    )
    unique_articles = []
    for story in agent_state["stories"]:
        if story["state"] != StoryState.RETRIEVED:
            continue
        story["articles"] = sort_articles_by_date(story["articles"])
        for article in story["articles"]:
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
        story["state"] = StoryState.CLEANED
    return agent_state
