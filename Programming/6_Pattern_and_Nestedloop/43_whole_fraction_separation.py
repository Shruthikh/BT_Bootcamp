def separate_whole_fraction(num):
    whole = int(num)
    fraction = num - whole
    return whole, fraction


if __name__ == "__main__":
    num = float(input("Enter a decimal number: "))
    whole, fraction = separate_whole_fraction(num)
    print("Whole part:", whole)
    print("Fractional part:", fraction)
