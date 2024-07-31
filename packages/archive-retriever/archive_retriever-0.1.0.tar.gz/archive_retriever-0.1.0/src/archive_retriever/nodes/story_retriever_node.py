import concurrent.futures
import uuid
from datetime import timedelta
from functools import partial

from langchain_cohere import CohereEmbeddings
from langchain_qdrant import Qdrant

from archive_retriever.state.agent_state import AgentState
from archive_retriever.state.article import get_datetime_of_document
from archive_retriever.state.article_state import ArticleState
from archive_retriever.state.story_state import StoryState
from archive_retriever.utilities.config import config
from archive_retriever.utilities.generate_qdrant_date_filter import (
    generate_qdrant_date_filter,
)


def story_retriever_node(agent_state: AgentState):
    embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")
    archive_vector_store = Qdrant.from_existing_collection(
        embeddings, collection_name="main", url=config.qdrant_url, timeout=300
    )

    def retrieve_and_check_documents(summary, start, end, top_k, check_every_x_days):
        documents = archive_vector_store.similarity_search(
            summary,
            k=top_k,
            filter=generate_qdrant_date_filter(start, end),
        )
        # Check if there's at least one document every x days
        should_evaluate = True
        for i in range(0, (end - start).days + 1, check_every_x_days):
            chunk_start = start + timedelta(days=i)
            chunk_end = min(chunk_start + timedelta(days=check_every_x_days), end)
            if not any(
                chunk_start <= get_datetime_of_document(doc) <= chunk_end
                for doc in documents
            ):
                should_evaluate = False
                break
        articles = [
            {
                "id": str(uuid.uuid4()),
                "state": ArticleState.RETRIEVED,
                "document": document,
            }
            for document in documents
        ]
        return {"should_evaluate": should_evaluate, "articles": articles}

    def process_story(story, config):
        if story["state"] != StoryState.INITIAL:
            return story
        past_result = retrieve_and_check_documents(
            story["summary"],
            story["date_time"] - timedelta(days=7),
            story["date_time"],
            config["story_week_top_k"],
            config["story_min_article_x_days"],
        )
        future_result = retrieve_and_check_documents(
            story["summary"],
            story["date_time"] + timedelta(days=1),
            story["date_time"] + timedelta(days=7),
            config["story_week_top_k"],
            config["story_min_article_x_days"],
        )
        story["articles"] = past_result["articles"] + future_result["articles"]
        if past_result["should_evaluate"]:
            very_past_result = retrieve_and_check_documents(
                story["summary"],
                story["date_time"] - timedelta(days=30),
                story["date_time"] - timedelta(days=8),
                config["story_month_top_k"],
                config["story_min_article_x_days"],
            )
            story["articles"] += very_past_result["articles"]
        if future_result["should_evaluate"]:
            very_future_result = retrieve_and_check_documents(
                story["summary"],
                story["date_time"] + timedelta(days=8),
                story["date_time"] + timedelta(days=30),
                config["story_month_top_k"],
                config["story_min_article_x_days"],
            )
            story["articles"] += very_future_result["articles"]
        story["state"] = StoryState.RETRIEVED
        return story

    with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
        process_story_partial = partial(
            process_story,
            config=agent_state["quality_config"],
        )
        updated_stories = list(
            thread_pool_executor.map(process_story_partial, agent_state["stories"])
        )
    agent_state["stories"] = updated_stories
    return agent_state
