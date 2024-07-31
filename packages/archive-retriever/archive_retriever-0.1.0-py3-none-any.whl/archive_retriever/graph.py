from langgraph.graph import END, StateGraph

from archive_retriever.edges.after_relevance_grader_conditional_edges import (
    after_relevance_grader_conditional_edges,
)
from archive_retriever.nodes.story_relevance_grader_node import (
    story_relevance_grader_node,
)
from archive_retriever.nodes.story_retrieval_cleaner_node import (
    story_retrieval_cleaner_node,
)
from archive_retriever.nodes.story_retrieval_planner_node import (
    story_retrieval_planner_node,
)
from archive_retriever.nodes.story_retriever_node import story_retriever_node
from archive_retriever.nodes.sub_topic_retrieval_planner_node import (
    sub_topic_retrieval_planner_node,
)
from archive_retriever.nodes.topic_relevance_grader_node import (
    topic_relevance_grader_node,
)
from archive_retriever.nodes.topic_retrieval_cleaner_node import (
    topic_retrieval_cleaner_node,
)
from archive_retriever.nodes.topic_retrieval_planner_node import (
    topic_retrieval_planner_node,
)
from archive_retriever.nodes.topic_retriever_node import topic_retriever_node
from archive_retriever.state.agent_state import AgentState

graph_builder = StateGraph(AgentState)

graph_builder.add_node("topic_retrieval_planner", topic_retrieval_planner_node)
graph_builder.add_node("topic_retriever", topic_retriever_node)
graph_builder.add_node("topic_retrieval_cleaner", topic_retrieval_cleaner_node)
graph_builder.add_node("topic_relevance_grader", topic_relevance_grader_node)
graph_builder.add_node("sub_topic_retrieval_planner", sub_topic_retrieval_planner_node)
graph_builder.add_node("sub_topic_retriever", topic_retriever_node)
graph_builder.add_node("sub_topic_retrieval_cleaner", topic_retrieval_cleaner_node)
graph_builder.add_node("sub_topic_relevance_grader", topic_relevance_grader_node)
graph_builder.add_node("story_retrieval_planner", story_retrieval_planner_node)
graph_builder.add_node("story_retriever", story_retriever_node)
graph_builder.add_node("story_retrieval_cleaner", story_retrieval_cleaner_node)
graph_builder.add_node("story_relevance_grader", story_relevance_grader_node)

graph_builder.add_edge("topic_retrieval_planner", "topic_retriever")
graph_builder.add_edge("topic_retriever", "topic_retrieval_cleaner")
graph_builder.add_edge("topic_retrieval_cleaner", "topic_relevance_grader")
graph_builder.add_conditional_edges(
    "topic_relevance_grader", after_relevance_grader_conditional_edges
)
graph_builder.add_edge("sub_topic_retrieval_planner", "sub_topic_retriever")
graph_builder.add_edge("sub_topic_retriever", "sub_topic_retrieval_cleaner")
graph_builder.add_edge("sub_topic_retrieval_cleaner", "sub_topic_relevance_grader")
graph_builder.add_edge("sub_topic_relevance_grader", "story_retrieval_planner")
graph_builder.add_edge("story_retrieval_planner", "story_retriever")
graph_builder.add_edge("story_retriever", "story_retrieval_cleaner")
graph_builder.add_edge("story_retrieval_cleaner", "story_relevance_grader")
graph_builder.add_edge("story_relevance_grader", END)

graph_builder.set_entry_point("topic_retrieval_planner")

graph = graph_builder.compile()
