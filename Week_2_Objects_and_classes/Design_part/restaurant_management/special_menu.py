from menu import Menu

# SpecialMenu IS-A Menu
class SpecialMenu(Menu):
    def __init__(self, menu_id, name):
        super().__init__(menu_id, name)
        self.discount = 30   # 30% discount
