# Topic class represents the subject area of a question
class Topic:
    def __init__(self, topic_id, topic_name):
        self.topic_id = topic_id
        self.topic_name = topic_name

    # Used while filtering questions by topic
    def get_topic_name(self):
        return self.topic_name
