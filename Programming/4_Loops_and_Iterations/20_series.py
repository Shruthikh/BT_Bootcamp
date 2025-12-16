# Coding Challenge 20: Display the Series 1,2,4,7,11,16,22...N

def print_incremental_series(n):
    value = 1
    diff = 1
    series = []

    for _ in range(n):
        series.append(str(value))
        value += diff
        diff += 1

    print(",".join(series))


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Invalid input.")
    else:
        print_incremental_series(n)
