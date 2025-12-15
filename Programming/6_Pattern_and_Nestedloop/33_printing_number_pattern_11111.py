def print_same_number_pattern(n):
    for i in range(1, n + 1):
        print(str(i) * n)


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_same_number_pattern(n)
