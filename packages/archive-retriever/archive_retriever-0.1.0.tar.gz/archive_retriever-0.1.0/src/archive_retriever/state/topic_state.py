from enum import Enum


class TopicState(Enum):
    INITIAL = "INITIAL"
    RETRIEVED = "RETRIEVED"
    CLEANED = "CLEANED"
    GRADED = "GRADED"
