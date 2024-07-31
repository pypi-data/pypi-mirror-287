class QualityConfig:
    def __init__(
        self,
        topic_generation_limit: int,
        topic_top_k: int,
        min_relevant_article_count_for_relevant_topic: int,
        min_relevant_topics: int,
        topic_limit: int,
        sub_topic_generation_limit: int,
        story_week_top_k: int,
        story_month_top_k: int,
        story_min_article_x_days: int,
        story_limit: int,
    ):
        self.topic_generation_limit = topic_generation_limit
        self.topic_top_k = topic_top_k
        self.min_relevant_article_count_for_relevant_topic = (
            min_relevant_article_count_for_relevant_topic
        )
        self.min_relevant_topics = min_relevant_topics
        self.topic_limit = topic_limit
        self.sub_topic_generation_limit = sub_topic_generation_limit
        self.story_week_top_k = story_week_top_k
        self.story_month_top_k = story_month_top_k
        self.story_min_article_x_days = story_min_article_x_days
        self.story_limit = story_limit
