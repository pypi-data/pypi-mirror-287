from typing import List, Optional, TypedDict

from .article import Article, format_article_to_text
from .topic_state import TopicState


class Topic(TypedDict):
    id: str
    state: TopicState
    parent_topic_id: Optional[str]
    title: str
    articles: Optional[List[Article]]
    is_relevant: Optional[bool]
    feedback: Optional[str]


def format_topics_to_inner_xml(topics):
    return "\n".join(
        [
            f"<Topic {i+1}>\n"
            + "\n".join(
                [
                    f"<Zeitungsartikel {j+1}>\n{format_article_to_text(article)}\n</Zeitungsartikel {j+1}>"
                    for j, article in enumerate(topic["articles"])
                    if article["is_relevant"]
                ]
            )
            + f"\n</Topic {i+1}>"
            for i, topic in enumerate(topics)
        ]
    )


def format_topics_to_feedback_text(topics):
    if len(topics) == 0:
        return "Dies ist der erste Durchlauf"
    return "\n".join(
        [
            f"{topic['title']}: {'Relevant' if topic['is_relevant'] else 'Irrelevant'}"
            for topic in topics
        ]
    )
    # return [
    #     {
    #         "topics": topic["title"],
    #         "is_relevant": topic["is_relevant"],
    #         # "feedback": topic["feedback"],
    #     }
    #     for topic in topics
    # ]
