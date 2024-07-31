from typing import List, Optional, TypedDict

from .article import Article, format_article_to_text
from .story_state import StoryState


class Story(TypedDict):
    id: str
    state: StoryState
    initial_article: Article
    title: str
    summary: str
    articles: Optional[List[Article]]


def format_stories_to_inner_xml(stories):
    return "\n".join(
        [
            f"<Story {i+1}>\n"
            + "\n".join(
                [
                    f"<Zeitungsartikel {j+1}>\n{format_article_to_text(article)}\n</Zeitungsartikel {j+1}>"
                    for j, article in enumerate(story["articles"])
                    if article["is_relevant"]
                ]
            )
            + f"\n</Story {i+1}>"
            for i, story in enumerate(stories)
        ]
    )
