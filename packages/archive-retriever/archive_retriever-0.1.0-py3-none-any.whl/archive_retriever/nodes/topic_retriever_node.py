import concurrent.futures
import uuid
from datetime import datetime
from functools import partial

from langchain_cohere import CohereEmbeddings
from langchain_qdrant import Qdrant

from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article_state import ArticleState
from archive_retriever.state.topic_state import TopicState
from archive_retriever.utilities.config import config
from archive_retriever.utilities.generate_qdrant_date_filter import (
    generate_qdrant_date_filter,
)


def topic_retriever_node(agent_state: AgentState):
    embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")
    archive_vector_store = Qdrant.from_existing_collection(
        embeddings, collection_name="main", url=config.qdrant_url, timeout=300
    )

    def process_topic(topic):
        if topic["state"] != TopicState.INITIAL:
            return topic
        documents = archive_vector_store.similarity_search(
            topic["title"],
            k=agent_state["quality_config"]["topic_top_k"],
            filter=generate_qdrant_date_filter(datetime(2000, 1, 1), datetime.now()),
        )
        topic["articles"] = [
            {
                "id": str(uuid.uuid4()),
                "state": ArticleState.RETRIEVED,
                "document": document,
            }
            for document in documents
        ]
        topic["state"] = TopicState.RETRIEVED
        return topic

    with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
        process_topic_partial = partial(process_topic)
        updated_topics = list(
            thread_pool_executor.map(process_topic_partial, agent_state["topics"])
        )
    agent_state["topics"] = updated_topics
    return agent_state
