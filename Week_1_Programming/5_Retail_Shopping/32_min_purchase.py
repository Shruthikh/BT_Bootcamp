# 32_min_purchase.py

if __name__ == "__main__":
    total = float(input("Enter Final Total: "))

    if total < 500:
        print("Minimum purchase of ₹500 not met. Invoice cannot be generated.")
    else:
        print("Minimum purchase met. Invoice generated.")
