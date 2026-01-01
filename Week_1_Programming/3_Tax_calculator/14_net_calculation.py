# Coding Challenge 14: Net Salary Calculation

def calculate_net_salary(annual_gross_salary, total_tax):
    return annual_gross_salary - total_tax


if __name__ == "__main__":
    annual_gross_salary = float(input("Enter Annual Gross Salary: "))
    total_tax = float(input("Enter Total Tax Payable: "))

    net_salary = calculate_net_salary(annual_gross_salary, total_tax)

    print("\n--- Net Salary ---")
    print("Annual Gross Salary: ₹", annual_gross_salary)
    print("Total Tax Payable: ₹", total_tax)
    print("Annual Net Salary: ₹", net_salary)
