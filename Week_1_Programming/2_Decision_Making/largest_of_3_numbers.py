def largest_of_three(a, b, c):
    return max(a, b, c)


if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))

        print("Largest number is", largest_of_three(a, b, c))
    except ValueError:
        print("Error: Enter numeric values.")
