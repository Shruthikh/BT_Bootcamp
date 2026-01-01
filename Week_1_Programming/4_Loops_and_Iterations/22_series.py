# Coding Challenge 22: Display the Series 1,4,7,12,23...N

def print_custom_series(n):
    value = 1
    diff = 3

    for _ in range(n):
        print(value, end=" ")
        value += diff
        diff = diff * 2 - 1


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_custom_series(n)
