# Represents a Menu
class Menu:
    def __init__(self, menu_id, name):
        self.menu_id = menu_id
        self.name = name
        self.categories = []   # HAS-A CourseCategory

    def add_category(self, category):
        self.categories.append(category)
