# OnlineExam acts as controller / manager
class OnlineExam:
    def __init__(self, exam_id):
        self.exam_id = exam_id

        # HAS-A relationship: OnlineExam HAS-A list of Questions
        self.questions = []

    # Used to add questions to the exam
    def add_question(self, question):
        self.questions.append(question)

    # -------------------------------
    # 1. Find total number of questions
    # -------------------------------
    def get_total_questions(self):
        # len() returns total number of questions
        return len(self.questions)

    # ------------------------------------
    # 2. List questions belonging to a topic
    # ------------------------------------
    def get_questions_by_topic(self, topic_name):
        result = []
        for q in self.questions:
            if q.get_topic().get_topic_name().lower() == topic_name.lower():
                result.append(q)
        return result

    # ------------------------------------------------
    # 3. List questions by topic AND category
    # ------------------------------------------------
    def get_questions_by_topic_and_category(self, topic_name, category_name):
        result = []
        for q in self.questions:
            if (q.get_topic().get_topic_name().lower() == topic_name.lower()
                    and q.get_category().get_category_name().lower() == category_name.lower()):
                result.append(q)
        return result
