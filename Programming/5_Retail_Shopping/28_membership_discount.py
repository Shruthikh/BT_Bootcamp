# 28_membership_discount.py

def apply_membership_discount(total, is_member):
    if is_member.lower() == 'y':
        total -= total * 0.02
    return total


if __name__ == "__main__":
    total = float(input("Enter Total Amount: "))
    member = input("Is customer a member? (y/n): ")

    final_total = apply_membership_discount(total, member)
    print("Final Total after Membership Discount: ₹", final_total)
