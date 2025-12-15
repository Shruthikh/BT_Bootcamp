# 49_array_search.py
# Search a given element in array

def search_element(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    key = int(input("Enter element to search: "))

    index = search_element(arr, key)

    if index == -1:
        print("Element not found")
    else:
        print("Element found at index:", index)
