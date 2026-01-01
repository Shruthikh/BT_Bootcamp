# Branch aggregates menus
class Branch:
    def __init__(self, location):
        self.location = location
        self.menus = []   # HAS-A Menu

    def add_menu(self, menu):
        self.menus.append(menu)
