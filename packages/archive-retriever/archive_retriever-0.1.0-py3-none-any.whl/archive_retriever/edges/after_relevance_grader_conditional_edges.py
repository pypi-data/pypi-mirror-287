from typing import Literal

from archive_retriever.state.agent_state import AgentState


def after_relevance_grader_conditional_edges(
    agent_state: AgentState,
) -> Literal["topic_retrieval_planner", "sub_topic_retrieval_planner"]:
    if (
        len([topic for topic in agent_state["topics"] if topic["is_relevant"]])
        < agent_state["quality_config"]["min_relevant_topics"]
        and len(agent_state["topics"]) < agent_state["quality_config"]["topic_limit"]
    ):
        return "topic_retrieval_planner"
    else:
        return "sub_topic_retrieval_planner"
