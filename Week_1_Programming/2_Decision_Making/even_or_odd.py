def check_even_odd(num):
    return "Even number" if num % 2 == 0 else "Odd number"


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(check_even_odd(num))
    except ValueError:
        print("Error: Please enter a valid integer.")
