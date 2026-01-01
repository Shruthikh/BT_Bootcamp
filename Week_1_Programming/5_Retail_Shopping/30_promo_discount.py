# 30_promo_discount.py

def apply_promo(item_code, total):
    if item_code == "PROMO10":
        total -= total * 0.10
    return total


if __name__ == "__main__":
    code = input("Enter Item Code: ")
    total = float(input("Enter Item Total: "))

    final_total = apply_promo(code, total)
    print("Item Total after Promo: ₹", final_total)
