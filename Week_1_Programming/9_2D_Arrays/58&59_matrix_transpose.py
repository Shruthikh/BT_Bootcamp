# 58_matrix_transpose.py

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)
    return transpose


if __name__ == "__main__":
    m = int(input("Enter rows: "))
    n = int(input("Enter columns: "))

    matrix = []
    for i in range(m):
        matrix.append(list(map(int, input().split())))

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("Transpose Matrix:")
    for row in transpose_matrix(matrix):
        print(row)
