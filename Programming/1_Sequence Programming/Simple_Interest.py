def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest using:
    SI = (Principal * Rate * Time) / 100
    """
    return (principal * rate * time) / 100


if __name__ == "__main__":
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest: "))
        time = float(input("Enter time : "))

        # Validation: business rule check
        if principal < 0 or rate < 0 or time < 0:
            print("Error: Principal, rate, and time must be non-negative values.")
        else:
            interest = calculate_simple_interest(principal, rate, time)
            print("Simple Interest =", interest)

    except ValueError:
        # Handles non-numeric input
        print("Error: Please enter valid numeric values only.")
