#  12: Taxable Income Calculation

STANDARD_DEDUCTION = 50000


def calculate_taxable_income(annual_gross_salary):
    return annual_gross_salary - STANDARD_DEDUCTION


if __name__ == "__main__":
    annual_gross_salary = float(input("Enter Annual Gross Salary: "))

    taxable_income = calculate_taxable_income(annual_gross_salary)

    print("\n--- Taxable Income Details ---")
    print("Annual Gross Salary: ₹", annual_gross_salary)
    print("Standard Deduction: ₹", STANDARD_DEDUCTION)
    print("Taxable Income: ₹", taxable_income)
