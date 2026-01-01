# 26_iterative_items.py

def calculate_item_total(qty, price):
    return qty * price


if __name__ == "__main__":
    grand_total = 0

    n = int(input("Enter number of items: "))

    for i in range(n):
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        grand_total += calculate_item_total(qty, price)

    print("\nGrand Total: ₹", grand_total)
