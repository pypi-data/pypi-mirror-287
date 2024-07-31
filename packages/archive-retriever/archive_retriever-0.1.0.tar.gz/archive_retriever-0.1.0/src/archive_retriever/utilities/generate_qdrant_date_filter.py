from datetime import datetime

from qdrant_client import models


def generate_qdrant_date_filter(start_date: datetime, end_date: datetime):
    return models.Filter(
        must=[
            models.FieldCondition(
                key="metadata.newspaper_published_year",
                range=models.Range(gte=start_date.year, lte=end_date.year),
            ),
            models.FieldCondition(
                key="metadata.newspaper_published_month",
                range=models.Range(gte=start_date.month, lte=end_date.month),
            ),
            models.FieldCondition(
                key="metadata.newspaper_published_day",
                range=models.Range(gte=start_date.day, lte=end_date.day),
            ),
        ]
    )
