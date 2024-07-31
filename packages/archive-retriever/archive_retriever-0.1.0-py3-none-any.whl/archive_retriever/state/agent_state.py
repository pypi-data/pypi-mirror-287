from typing import List, TypedDict


from .story import Story
from .topic import Topic


class AgentState(TypedDict):
    quality_config: any
    query: str
    topics: List[Topic]
    stories: List[Story]
