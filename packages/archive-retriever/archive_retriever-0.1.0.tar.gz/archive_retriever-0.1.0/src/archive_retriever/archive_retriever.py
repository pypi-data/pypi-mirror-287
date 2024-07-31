import uuid
from typing import List

from langchain_core.documents import Document

from archive_retriever.graph import graph
from archive_retriever.quality_config import QualityConfig
from archive_retriever.state.article import check_are_articles_equal
from archive_retriever.state.topic_state import TopicState


class ArchiveRetriever:
    def __init__(self, quality_config: QualityConfig):
        self._quality_config = quality_config

    def retrieve(self, query: str) -> List[Document]:
        result = graph.invoke(
            {
                "quality_config": vars(self._quality_config),
                "query": query,
                "topics": [
                    {
                        "id": str(uuid.uuid4()),
                        "state": TopicState.INITIAL,
                        "title": query,
                        "is_relevant": True,
                        "feedback": "Dies ist die rohe Nutzeranfrage",
                    }
                ],
                "stories": [],
            },
            config={
                "recursion_limit": 100,
            },
        )
        articles = []
        for source in result["topics"] + result["stories"]:
            for article in source["articles"]:
                if (
                    not article["is_relevant"]
                    or article["is_doubled"]
                    or any(
                        check_are_articles_equal(article, existing_article)
                        for existing_article in articles
                    )
                ):
                    continue
                articles.append(article)
        documents = [
            Document(
                page_content=article["text"], metadata=article["document"].metadata
            )
            for article in articles
        ]
        return documents
