# 52_reverse_array.py
# Level 1: Reverse the array

def reverse_array(arr):
    return arr[::-1]


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))

    if len(arr) == 0:
        print("Array is empty")
    else:
        print("Reversed array:", reverse_array(arr))
