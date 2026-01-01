# 54_binary_search.py
# Level 3: Binary Search on array

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted array elements: ").split()))
    key = int(input("Enter element to search: "))

    index = binary_search(arr, key)

    if index == -1:
        print("Element not found")
    else:
        print("Element found at index:", index)
