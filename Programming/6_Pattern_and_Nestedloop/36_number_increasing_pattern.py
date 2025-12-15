def print_number_increasing(n):
    for i in range(1, n + 1):
        print(str(i) * i)


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_number_increasing(n)
