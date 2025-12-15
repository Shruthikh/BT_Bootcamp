# 27_discounts.py

def apply_discounts(total, total_quantity):
    if total > 10000:
        total -= total * 0.10

    if total_quantity > 20:
        total -= total * 0.05

    return total


if __name__ == "__main__":
    total = float(input("Enter Grand Total: "))
    quantity = int(input("Enter Total Quantity: "))

    final_total = apply_discounts(total, quantity)
    print("Total after Discounts: ₹", final_total)
