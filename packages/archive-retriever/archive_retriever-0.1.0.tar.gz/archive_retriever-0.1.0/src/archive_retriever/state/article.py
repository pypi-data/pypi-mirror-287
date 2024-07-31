from datetime import datetime
from typing import Optional, TypedDict

from langchain_core.documents import Document

from .article_state import ArticleState


class Article(TypedDict):
    state: ArticleState
    document: Document
    text: Optional[str]
    is_relevant: Optional[bool]
    feedback: Optional[str]
    is_doubled: Optional[bool]
    unique_article_id: Optional[str]


def check_are_articles_equal(article_a, article_b):
    return (
        article_a["document"].metadata["article_unique_id"]
        == article_b["document"].metadata["article_unique_id"]
    )


def get_datetime_of_document(document):
    return datetime(
        int(document.metadata["newspaper_published_year"]),
        int(document.metadata["newspaper_published_month"]),
        int(document.metadata["newspaper_published_day"]),
    )


def get_datetime_of_article(article):
    return get_datetime_of_document(article["document"])


def format_article_to_text(article):
    return f"Newspaper number: {article['document'].metadata['newspaper_number']}\nNewspaper type: {article['document'].metadata['newspaper_type']}\nNewspaper published date: {article['document'].metadata['newspaper_published_year']}-{article['document'].metadata['newspaper_published_month']}-{article['document'].metadata['newspaper_published_day']}\nNewspaper page: {article['document'].metadata['newspaper_page']}\n\nText:\n{article['document'].page_content}"


def format_articles_to_inner_xml(articles):
    return "\n".join(
        [
            f"<Zeitungsartikel {i+1}>\n{format_article_to_text(article)}\n</Zeitungsartikel {i+1}>"
            for i, article in enumerate(articles)
        ]
    )


def sort_articles_by_date(articles):
    return sorted(
        articles,
        key=lambda x: (
            x["document"].metadata["newspaper_published_year"],
            x["document"].metadata["newspaper_published_month"],
            x["document"].metadata["newspaper_published_day"],
        ),
    )
