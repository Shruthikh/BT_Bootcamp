# 55_2d_array_display.py

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    if r <= 0 or c <= 0:
        print("Invalid matrix size")
    else:
        mat = read_matrix(r, c)
        print("Matrix (Row-wise):")
        display_matrix(mat)
