from topic import Topic
from category import Category
from mcq_question import MCQQuestion
from paragraph_question import ParagraphQuestion
from online_exam import OnlineExam

def main():
    # Create Topic and Category objects
    java_topic = Topic(1, "Java")
    easy_category = Category(1, "Easy")

    # Create MCQ Question
    q1 = MCQQuestion(
        101,
        "What is JVM?",
        java_topic,
        easy_category,
        ["Java Virtual Machine", "Java Variable Method"],
        "Java Virtual Machine"
    )

    # Create Paragraph Question
    q2 = ParagraphQuestion(
        102,
        "Explain OOPS concepts",
        java_topic,
        easy_category,
        200
    )

    # Create Online Exam
    exam = OnlineExam(1)

    # Add questions to exam
    exam.add_question(q1)
    exam.add_question(q2)

    # -------- OUTPUTS --------

    # 1. Total number of questions
    print("Total Questions:", exam.get_total_questions())

    # 2. Questions by Topic
    print("\nQuestions belonging to topic 'Java':")
    for q in exam.get_questions_by_topic("Java"):
        print("-", q.get_question_text())

    # 3. Questions by Topic and Category
    print("\nQuestions belonging to topic 'Java' and category 'Easy':")
    for q in exam.get_questions_by_topic_and_category("Java", "Easy"):
        print("-", q.get_question_text())

# Entry point
if __name__ == "__main__":
    main()
