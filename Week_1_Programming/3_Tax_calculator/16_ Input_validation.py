# Coding Challenge 16: Input Validation Rules

def validate_name(name):
    return name.isalpha() and len(name) <= 50


def validate_emp_id(emp_id):
    return emp_id.isalnum() and 5 <= len(emp_id) <= 10


def validate_salary(value):
    return value > 0 and value <= 10000000


def validate_bonus(bonus):
    return 0 <= bonus <= 100


if __name__ == "__main__":

    while True:
        name = input("Enter Name: ")
        if validate_name(name):
            break
        print("Invalid Name. Try again.")

    while True:
        emp_id = input("Enter Employee ID: ")
        if validate_emp_id(emp_id):
            break
        print("Invalid Employee ID. Try again.")

    while True:
        basic_salary = float(input("Enter Basic Salary: "))
        if validate_salary(basic_salary):
            break
        print("Invalid Salary. Try again.")

    while True:
        bonus = float(input("Enter Bonus Percentage: "))
        if validate_bonus(bonus):
            break
        print("Invalid Bonus Percentage. Try again.")

    print("\nAll inputs are valid ✅")
