# Represents course category like Starters, Main Course, Desserts
class CourseCategory:
    def __init__(self, name):
        self.name = name
        self.items = []   # HAS-A MenuItem

    def add_item(self, item):
        self.items.append(item)
