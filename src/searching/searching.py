def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i

    return -1


def binary_search(arr, target):
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr)-1

    while low <= high:
        midpoint = (low + high) // 2

        if arr[midpoint] == target:
            return arr.index(target)

        if target < arr[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1

    return -1  # not found


def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1

    if low > high:
        return -1

    middle = (low + high) // 2

    if arr[middle] == target:
        return arr.index(target)

    if target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle - 1)
    else:
        return binary_search_recursive(arr, target, middle + 1, high)
