# 57_2d_array_search.py

def search_element(matrix, key):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == key:
                return i, j
    return None


if __name__ == "__main__":
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    matrix = []
    for i in range(r):
        matrix.append(list(map(int, input().split())))

    key = int(input("Enter element to search: "))
    result = search_element(matrix, key)

    if result:
        print(f"Element found at position {result}")
    else:
        print("Element not found")
