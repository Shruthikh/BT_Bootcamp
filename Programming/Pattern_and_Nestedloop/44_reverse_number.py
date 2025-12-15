def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev


if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Reversed number:", reverse_number(num))
