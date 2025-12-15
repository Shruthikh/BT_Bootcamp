# 56_2d_array_sum.py

def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total


if __name__ == "__main__":
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    matrix = []
    for i in range(r):
        matrix.append(list(map(int, input().split())))

    print("Sum of all elements:", sum_matrix(matrix))
