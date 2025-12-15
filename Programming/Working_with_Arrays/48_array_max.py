# 48_array_max.py
# Find maximum element in array

def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print("Maximum value:", find_max(arr))
