# Coding Challenge 15: Report Generation

def generate_report(name, emp_id, gross_monthly, annual_gross,
                    taxable_income, tax_payable, net_salary):

    print("\n========== Employee Tax Report ==========")
    print("Name               :", name)
    print("EmpID              :", emp_id)
    print("Gross Monthly      : ₹", gross_monthly)
    print("Annual Gross       : ₹", annual_gross)
    print("Taxable Income     : ₹", taxable_income)
    print("Tax Payable        : ₹", tax_payable)
    print("Annual Net Salary  : ₹", net_salary)
    print("========================================")


if __name__ == "__main__":
    generate_report(
        "John Doe", "E12345",
        85000, 1020000,
        970000, 76800,
        943200
    )
