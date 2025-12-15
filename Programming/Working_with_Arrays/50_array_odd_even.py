# 50_array_odd_even.py
# Count odd and even numbers in array

def count_odd_even(arr):
    odd = even = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))

    odd, even = count_odd_even(arr)
    print("Odd count:", odd)
    print("Even count:", even)
