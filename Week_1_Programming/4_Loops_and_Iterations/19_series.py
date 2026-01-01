# 19_series.py
# Coding Challenge 19: Display the Series 4,16,36,64...N

def print_even_square_series(n):
    for i in range(2, n + 1, 2):
        print(i * i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter N: "))

    if n < 2:
        print("No terms to display.")
    else:
        print_even_square_series(n)
