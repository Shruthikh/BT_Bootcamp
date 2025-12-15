# 20_series.py
# Coding Challenge 20: Display the Series 1,2,4,7,11,16,22...N

def print_incremental_series(n):
    value = 1
    diff = 1

    for _ in range(n):
        print(value, end=" ")
        diff += 1
        value += diff


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_incremental_series(n)
