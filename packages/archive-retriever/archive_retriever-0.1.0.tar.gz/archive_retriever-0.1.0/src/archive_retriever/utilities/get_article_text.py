from contextlib import contextmanager
from functools import lru_cache

from psycopg2.pool import SimpleConnectionPool

from .config import config

db_pool = SimpleConnectionPool(1, 20, config.db_url)


@contextmanager
def get_db_connection():
    connection = db_pool.getconn()
    try:
        yield connection
    finally:
        db_pool.putconn(connection)


@lru_cache(maxsize=1000)
def get_article_text_by_unique_id(article_unique_id):
    with get_db_connection() as db_connection:
        with db_connection.cursor() as db_cursor:
            db_cursor.execute(
                "SELECT text FROM articles WHERE unique_id = %s", (article_unique_id,)
            )
            article_text = db_cursor.fetchone()[0]
    return article_text


def get_article_text(article):
    return get_article_text_by_unique_id(
        article["document"].metadata["article_unique_id"]
    )
