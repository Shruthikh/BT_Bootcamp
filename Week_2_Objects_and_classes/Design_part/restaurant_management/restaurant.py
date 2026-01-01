from billing_service import BillingService
from special_menu import SpecialMenu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.branches = []          # HAS-A Branch
        self.billing = BillingService()  # USES BillingService

    def add_branch(self, branch):
        self.branches.append(branch)

    # 1️⃣ Total number of menu items
    def total_menu_items(self):
        count = 0
        for branch in self.branches:
            for menu in branch.menus:
                for category in menu.categories:
                    count += len(category.items)
        return count

    # 2️⃣ Print ALL menu items grouped by category
    def print_all_items_by_category(self):
        category_map = {}

        for branch in self.branches:
            for menu in branch.menus:
                for category in menu.categories:
                    if category.name not in category_map:
                        category_map[category.name] = []
                    category_map[category.name].extend(category.items)

        for category_name, items in category_map.items():
            print("\nCategory:", category_name)
            for item in items:
                print("-", item.name, "Rs.", item.price)

    # 3️⃣ List all special discount menus
    def special_menus(self):
        result = []
        for branch in self.branches:
            for menu in branch.menus:
                if isinstance(menu, SpecialMenu):
                    result.append(menu)
        return result
