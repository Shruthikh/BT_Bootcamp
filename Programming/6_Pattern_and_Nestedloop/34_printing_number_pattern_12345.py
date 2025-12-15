def print_number_sequence(n):
    for _ in range(n):
        for j in range(1, n + 1):
            print(j, end="")
        print()


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_number_sequence(n)
