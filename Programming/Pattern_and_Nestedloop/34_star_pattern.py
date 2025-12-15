def print_star_pattern(n):
    for _ in range(n):
        print("*" * n)


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_star_pattern(n)
