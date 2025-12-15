# Coding Challenge 11: Basic Input and Salary Calculation

def calculate_gross_salary(basic_salary, special_allowance, bonus_percent):
    gross_monthly = basic_salary + special_allowance
    annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus
    return gross_monthly, annual_gross


if __name__ == "__main__":
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")

    basic_salary = float(input("Enter Basic Monthly Salary: "))
    special_allowance = float(input("Enter Special Allowance (Monthly): "))
    bonus_percent = float(input("Enter Bonus Percentage: "))

    gross_monthly, annual_gross = calculate_gross_salary(
        basic_salary, special_allowance, bonus_percent
    )

    print("\n--- Employee Salary Details ---")
    print("Name:", name)
    print("EmpID:", emp_id)
    print("Gross Monthly Salary: ₹", gross_monthly)
    print("Annual Gross Salary: ₹", annual_gross)
