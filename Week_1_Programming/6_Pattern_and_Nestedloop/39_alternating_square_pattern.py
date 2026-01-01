def print_alternating_squares(n):
    num = 1
    sign = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(sign * (num * num), end=" ")
            sign *= -1
            num += 1
        print()


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_alternating_squares(n)
