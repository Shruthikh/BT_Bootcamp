# 47_array_min.py
# Find minimum element in array

def find_min(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print("Minimum value:", find_min(arr))
