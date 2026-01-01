# 18_series.py
# Coding Challenge 18: Display the Series 1,3,5,7,9...N

def print_odd_series(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter N: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_odd_series(n)
