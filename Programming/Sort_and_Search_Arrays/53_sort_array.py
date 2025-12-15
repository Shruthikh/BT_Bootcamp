# 53_sort_array.py
# Level 2: Sort array based on user choice

def sort_array(arr, order):
    if order == "asc":
        return sorted(arr)
    elif order == "desc":
        return sorted(arr, reverse=True)
    else:
        return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    order = input("Enter sorting order (asc/desc): ").lower()

    sorted_arr = sort_array(arr, order)

    if sorted_arr is None:
        print("Invalid sorting option")
    else:
        print("Sorted array:", sorted_arr)
