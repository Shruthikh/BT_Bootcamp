# Coding Challenge 13: Tax and Rebate Calculation

def calculate_tax(taxable_income):
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
    taxable_income = float(input("Enter Taxable Income: "))

    tax, cess, total_tax = calculate_tax(taxable_income)

    print("\n--- Tax Breakdown ---")
    print("Tax Payable: ₹", tax)
    print("Cess (4%): ₹", cess)
    print("Total Tax Payable: ₹", total_tax)
