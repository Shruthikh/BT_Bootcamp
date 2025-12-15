def swap_numbers(a, b):
    
    return b, a


if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        swapped_a, swapped_b = swap_numbers(num1, num2)

        print("After swapping:")
        print("First number =", swapped_a)
        print("Second number =", swapped_b)

    except ValueError:
        print("Error: Please enter valid numeric values only.")
