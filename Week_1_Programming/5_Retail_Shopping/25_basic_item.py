# 25_basic_item.py

def calculate_item_total(quantity, price):
    return quantity * price


if __name__ == "__main__":
    item_code = input("Enter Item Code: ")
    description = input("Enter Description: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    total = calculate_item_total(quantity, price)

    print("\nItem Code:", item_code)
    print("Description:", description)
    print("Item Total: ₹", total)
