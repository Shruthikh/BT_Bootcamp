# 17_series.py
# Coding Challenge 17: Display the Series 1,2,3,4,5...N

def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter N: "))

    if n <= 0:
        print("Invalid input. N must be positive.")
    else:
        print_natural_numbers(n)
