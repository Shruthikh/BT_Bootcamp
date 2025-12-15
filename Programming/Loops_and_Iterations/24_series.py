# 24_series.py
# Coding Challenge 24: Display the Fibonacci Series

def print_fibonacci_series(n):
    a, b = 1, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_fibonacci_series(n)
