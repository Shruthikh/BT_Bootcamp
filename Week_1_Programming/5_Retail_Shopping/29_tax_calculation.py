# 29_tax_calculation.py

def calculate_tax(total):
    if total < 5000:
        return total * 0.05
    elif total <= 20000:
        return total * 0.10
    else:
        return total * 0.15


if __name__ == "__main__":
    total = float(input("Enter Grand Total: "))
    tax = calculate_tax(total)

    print("Tax Amount: ₹", tax)
    print("Total with Tax: ₹", total + tax)
