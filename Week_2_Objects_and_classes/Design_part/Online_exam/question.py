# Base class for all types of questions
class Question:
    def __init__(self, question_id, question_text, topic, category):
        self.question_id = question_id
        self.question_text = question_text

        # HAS-A relationship
        self.topic = topic          # Question HAS-A Topic
        self.category = category    # Question HAS-A Category

    # Getter used in filtering by topic
    def get_topic(self):
        return self.topic

    # Getter used in filtering by category
    def get_category(self):
        return self.category

    def get_question_text(self):
        return self.question_text
