# 23_series.py
# Coding Challenge 23: Display the Series 1,5,9,...

def print_mixed_series(n):
    value = 1

    for i in range(n):
        print(value, end=" ")
        if i % 4 == 3:
            value += 8
        else:
            value += 4


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_mixed_series(n)
