# 31_payment_mode.py

def apply_payment_surcharge(total, payment_mode):
    surcharge = 0
    if payment_mode.lower() == "credit":
        surcharge = total * 0.02
    return surcharge


if __name__ == "__main__":
    total = float(input("Enter Total Amount: "))
    mode = input("Payment Mode (cash/credit): ")

    surcharge = apply_payment_surcharge(total, mode)
    print("Surcharge: ₹", surcharge)
    print("Final Payable Amount: ₹", total + surcharge)
