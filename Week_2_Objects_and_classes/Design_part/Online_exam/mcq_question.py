from question import Question

# MCQQuestion IS-A Question
class MCQQuestion(Question):
    def __init__(self, question_id, question_text,
                 topic, category, options, correct_option):

        # Calling parent (Question) constructor
        super().__init__(question_id, question_text, topic, category)

        self.options = options
        self.correct_option = correct_option
