# ============================================================
# File Name: 25_33_retail_shopping_app.py
# Retail Shopping Application – Coding Challenges 25 to 33
# ============================================================

# -------------------- FUNCTIONS --------------------

def calculate_item_total(quantity, price):
    return quantity * price


def apply_promo_discount(item_code, item_total):
    if item_code.upper() == "PROMO10":
        discount = item_total * 0.10
        return item_total - discount, discount
    return item_total, 0


def apply_bulk_discounts(grand_total, total_quantity):
    discount = 0
    if grand_total > 10000:
        discount += grand_total * 0.10
        grand_total -= grand_total * 0.10

    if total_quantity > 20:
        discount += grand_total * 0.05
        grand_total -= grand_total * 0.05

    return grand_total, discount


def apply_membership_discount(grand_total, is_member):
    if is_member.lower() == 'y':
        discount = grand_total * 0.02
        return grand_total - discount, discount
    return grand_total, 0


def calculate_tax(grand_total):
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax = grand_total * tax_rate
    return tax, tax_rate


def apply_payment_surcharge(grand_total, payment_mode):
    if payment_mode.lower() == "credit":
        surcharge = grand_total * 0.02
        return surcharge
    return 0


def calculate_loyalty_points(final_total):
    return int(final_total // 100)


# -------------------- MAIN EXECUTION --------------------

if __name__ == "__main__":

    print("=== Retail Shopping Application ===")

    items = []
    grand_total = 0
    total_quantity = 0
    total_promo_discount = 0

    n = int(input("Enter number of items: "))

    for i in range(n):
        print(f"\nItem {i + 1}")
        item_code = input("Enter Item Code: ")
        description = input("Enter Description: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        item_total = calculate_item_total(quantity, price)
        item_total, promo_discount = apply_promo_discount(item_code, item_total)

        total_promo_discount += promo_discount
        grand_total += item_total
        total_quantity += quantity

        items.append((item_code, description, quantity, price, item_total))

    # Apply bulk & quantity discounts
    grand_total, bulk_discount = apply_bulk_discounts(grand_total, total_quantity)

    # Membership discount
    member = input("\nIs customer a member? (y/n): ")
    grand_total, member_discount = apply_membership_discount(grand_total, member)

    # Tax calculation
    tax, tax_rate = calculate_tax(grand_total)
    grand_total_with_tax = grand_total + tax

    # Payment mode
    payment_mode = input("Payment Mode (cash/credit): ")
    surcharge = apply_payment_surcharge(grand_total_with_tax, payment_mode)
    final_total = grand_total_with_tax + surcharge

    # Minimum purchase check
    if final_total < 500:
        print("\nMinimum purchase of ₹500 not met. Invoice cannot be generated.")
        exit()

    # Loyalty points
    loyalty_points = calculate_loyalty_points(final_total)

    # -------------------- INVOICE --------------------

    print("\n================ INVOICE ================")
    print("Items Purchased:")
    print("Code\tQty\tPrice\tTotal")

    for item in items:
        print(f"{item[0]}\t{item[2]}\t{item[3]}\t{item[4]}")

    print("-----------------------------------------")
    print("Promo Discount Applied: ₹", total_promo_discount)
    print("Bulk/Quantity Discount: ₹", bulk_discount)
    print("Membership Discount: ₹", member_discount)
    print("Tax (", int(tax_rate * 100), "% ): ₹", tax)
    print("Payment Surcharge: ₹", surcharge)
    print("-----------------------------------------")
    print("Final Payable Amount: ₹", final_total)
    print("Loyalty Points Earned:", loyalty_points)
    print("=========================================")
