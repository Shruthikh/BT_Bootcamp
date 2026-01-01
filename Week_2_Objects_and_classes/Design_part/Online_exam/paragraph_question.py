from question import Question

# ParagraphQuestion IS-A Question
class ParagraphQuestion(Question):
    def __init__(self, question_id, question_text,
                 topic, category, word_limit):

        # Calling parent (Question) constructor
        super().__init__(question_id, question_text, topic, category)

        self.word_limit = word_limit
