# 21_series.py
# Coding Challenge 21: Display the Series 1,4,9,25,36,49,81...N

def print_square_series(n):
    for i in range(1, n + 1):
        print(i * i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter N: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_square_series(n)
