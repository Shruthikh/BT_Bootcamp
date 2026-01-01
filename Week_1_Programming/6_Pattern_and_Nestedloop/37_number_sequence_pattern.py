def print_sequence_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_sequence_pattern(n)
