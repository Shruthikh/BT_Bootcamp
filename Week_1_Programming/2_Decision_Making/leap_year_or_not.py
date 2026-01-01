def is_leap_year(year):
    if year <= 0:
        return "Invalid year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    return "Not a leap year"


if __name__ == "__main__":
    try:
        year = int(input("Enter year: "))
        print(is_leap_year(year))
    except ValueError:
        print("Error: Enter valid year.")
