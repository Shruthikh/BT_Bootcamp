# Category class represents difficulty/type grouping of questions
class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    # Used while filtering questions by category
    def get_category_name(self):
        return self.category_name
