def calculate_discount(total_amount):
   
    if total_amount >= 1000:
        return total_amount * 0.10
    return 0.0


if __name__ == "__main__":
    try:
        total_amount = float(input("Enter total amount: "))

        if total_amount < 0:
            print("Error: Total amount cannot be negative.")
        else:
            discount = calculate_discount(total_amount)
            final_amount = total_amount - discount

            print("Discount =", discount)
            print("Final Amount =", final_amount)

    except ValueError:
        print("Error: Please enter a valid numeric amount.")
