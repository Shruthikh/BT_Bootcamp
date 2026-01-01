# 33_loyalty_points.py

def calculate_loyalty_points(total):
    return int(total // 100)


if __name__ == "__main__":
    total = float(input("Enter Final Total: "))

    points = calculate_loyalty_points(total)
    print("Loyalty Points Earned:", points)
