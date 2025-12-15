# 46_array_sum.py
# Find sum of array elements

def find_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print("Sum of elements:", find_sum(arr))
