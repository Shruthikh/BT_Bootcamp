def calculate_sum_and_average(a, b):
    
    total = a + b
    average = total / 2
    return total, average


if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        total, avg = calculate_sum_and_average(num1, num2)

        # Output
        print(f"Sum = {total}")
        print(f"Average = {avg}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
