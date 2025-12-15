# 60_matrix_multiplication.py

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


if __name__ == "__main__":
    r1 = int(input("Enter rows of matrix A: "))
    c1 = int(input("Enter columns of matrix A: "))
    r2 = int(input("Enter rows of matrix B: "))
    c2 = int(input("Enter columns of matrix B: "))

    if c1 != r2:
        print("Matrix multiplication not possible")
    else:
        print("Enter Matrix A:")
        A = [list(map(int, input().split())) for _ in range(r1)]

        print("Enter Matrix B:")
        B = [list(map(int, input().split())) for _ in range(r2)]

        result = multiply_matrices(A, B)

        print("Resultant Matrix:")
        for row in result:
            print(row)
