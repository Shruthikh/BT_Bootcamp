
# 11: Basic Input & Salary Calculation
# - Accept employee details
# - Calculate gross monthly & annual salary


def calculate_gross_salary(basic_salary, special_allowance, bonus_percent):
    gross_monthly = basic_salary + special_allowance
    annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus
    return gross_monthly, annual_gross



#  12: Taxable Income Calculation
# - Apply standard deduction
# - Compute taxable income


def calculate_taxable_income(annual_gross_salary):
    STANDARD_DEDUCTION = 50000
    return annual_gross_salary - STANDARD_DEDUCTION



#  13: Tax & Rebate Calculation
# - Apply New Tax Regime 2023 slabs
# - Apply Section 87A rebate
# - Add 4% Health & Education Cess


def calculate_tax(taxable_income):
    tax = 0

    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = 15000 + (taxable_income - 600000) * 0.10
    elif taxable_income <= 1200000:
        tax = 45000 + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = 90000 + (taxable_income - 1200000) * 0.20
    else:
        tax = 150000 + (taxable_income - 1500000) * 0.30

    # Section 87A Rebate
    if taxable_income <= 700000:
        tax = 0

    cess = tax * 0.04
    total_tax = tax + cess
    return tax, cess, total_tax


if __name__ == "__main__":

    # -------- Input Validation --------

    name = input("Enter Employee Name: ")
    if not name.isalpha() or len(name) > 50:
        print("Invalid Name")
        exit()

    emp_id = input("Enter Employee ID: ")
    if not emp_id.isalnum() or not (5 <= len(emp_id) <= 10):
        print("Invalid Employee ID")
        exit()

    basic_salary = float(input("Enter Basic Monthly Salary: "))
    if basic_salary <= 0 or basic_salary > 10000000:
        print("Invalid Basic Salary")
        exit()

    special_allowance = float(input("Enter Special Allowance (Monthly): "))
    if special_allowance < 0 or special_allowance > 10000000:
        print("Invalid Special Allowance")
        exit()

    bonus_percent = float(input("Enter Bonus Percentage: "))
    if bonus_percent < 0 or bonus_percent > 100:
        print("Invalid Bonus Percentage")
        exit()

    # -------- Coding Challenge 11: Salary Calculation --------

    gross_monthly, annual_gross = calculate_gross_salary(
        basic_salary, special_allowance, bonus_percent
    )

    # -------- Coding Challenge 12: Taxable Income --------

    taxable_income = calculate_taxable_income(annual_gross)

    # -------- Coding Challenge 13: Tax Calculation --------

    tax, cess, total_tax = calculate_tax(taxable_income)

    # -------- Coding Challenge 14: Net Salary --------

    net_salary = annual_gross - total_tax

    # -------- Coding Challenge 15: Report Generation --------

    print("\n========== Employee Tax Report ==========")
    print("Name                :", name)
    print("EmpID               :", emp_id)
    print("Gross Monthly Salary: ₹", gross_monthly)
    print("Annual Gross Salary : ₹", annual_gross)
    print("Taxable Income      : ₹", taxable_income)
    print("Tax Payable         : ₹", tax)
    print("Cess (4%)           : ₹", cess)
    print("Total Tax Payable   : ₹", total_tax)
    print("Annual Net Salary   : ₹", net_salary)
    print("========================================")
