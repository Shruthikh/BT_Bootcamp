from restaurant import Restaurant
from branch import Branch
from menu import Menu
from special_menu import SpecialMenu
from course_category import CourseCategory
from menu_item import MenuItem

def main():
    # Create Restaurant
    restaurant = Restaurant("Food Hub")

    # Create Branch
    branch = Branch("Bangalore")

    # Create Menus
    regular_menu = Menu(1, "Regular Menu")
    festival_menu = SpecialMenu(2, "Festival Menu")

    # Create Course Categories (minimum 3)
    starters = CourseCategory("Starters")
    main_course = CourseCategory("Main Course")
    desserts = CourseCategory("Desserts")

    # Add items to Starters
    starters.add_item(MenuItem("Soup", 100))
    starters.add_item(MenuItem("Paneer Tikka", 180))
    starters.add_item(MenuItem("Veg Cutlet", 120))

    # Add items to Main Course
    main_course.add_item(MenuItem("Veg Biryani", 250))
    main_course.add_item(MenuItem("Butter Naan", 60))
    main_course.add_item(MenuItem("Paneer Butter Masala", 220))

    # Add items to Desserts
    desserts.add_item(MenuItem("Ice Cream", 120))
    desserts.add_item(MenuItem("Gulab Jamun", 90))
    desserts.add_item(MenuItem("Brownie", 150))

    # Add categories to menus
    for cat in [starters, main_course, desserts]:
        regular_menu.add_category(cat)
        festival_menu.add_category(cat)

    # Add menus to branch
    branch.add_menu(regular_menu)
    branch.add_menu(festival_menu)

    # Add branch to restaurant
    restaurant.add_branch(branch)

    # ---------------- OUTPUTS ----------------
    print("Total menu items:", restaurant.total_menu_items())

    print("\nAll Menu Items Based on Category:")
    restaurant.print_all_items_by_category()

    print("\nSpecial Discount Menus:")
    for sm in restaurant.special_menus():
        print("-", sm.name, "Discount:", sm.discount, "%")

if __name__ == "__main__":
    main()
