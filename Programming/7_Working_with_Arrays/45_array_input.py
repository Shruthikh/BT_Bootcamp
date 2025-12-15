# 45_array_input.py
# Accept n and store n elements in an array

def read_array(n):
    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))
    return arr


if __name__ == "__main__":
    n = int(input("Enter size of array: "))

    if n <= 0:
        print("Invalid array size")
    else:
        array = read_array(n)
        print("Array elements:", array)
