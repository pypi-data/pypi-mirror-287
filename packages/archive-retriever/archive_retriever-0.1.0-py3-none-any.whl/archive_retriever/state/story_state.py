from enum import Enum


class StoryState(Enum):
    INITIAL = "INITIAL"
    RETRIEVED = "RETRIEVED"
    CLEANED = "CLEANED"
    GRADED = "GRADED"
