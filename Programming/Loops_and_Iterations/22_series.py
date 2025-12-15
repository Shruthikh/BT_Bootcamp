# 22_series.py
# Coding Challenge 22: Display the Series 1,4,7,12,23...N

def print_custom_series(n):
    value = 1

    for i in range(n):
        print(value, end=" ")
        value += (2 * i + 1)


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_custom_series(n)
