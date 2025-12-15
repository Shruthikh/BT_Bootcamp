def print_star_increasing(n):
    for i in range(1, n + 1):
        print("*" * i)


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_star_increasing(n)
