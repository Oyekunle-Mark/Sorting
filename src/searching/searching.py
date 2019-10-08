def linear_search(arr, target):
    """A basic linear search algorithm

    Arguments:
        arr {list} -- the list to be searched
        target {int} --the number to be searched for

    Returns:
        int -- -1 if target not found in arr and 1 if found
    """
    for i, item in enumerate(arr):
        if item == target:
            return i

    return -1


def binary_search(arr, target):
    """An implementation of the binary search algorithm

    Arguments:
                arr {list} -- the list to be searched
                target {int} --the number to be searched for

        Returns:
    int -- -1 if target not found in arr and 1 if found
    """
    # if array is empty
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
    """A recursive binary search algorithm

    Arguments:
            arr {list} -- the list to be searched
    target {int} --the number to be searched for
            low {int} -- the start index
            high {int} -- the end index

    Returns:
    int -- -1 if target not found in arr and 1 if found
    """
    # if array is empty
    if len(arr) == 0:
        return -1

    # base case
    if low > high:
        return -1

    middle = (low + high) // 2

    if arr[middle] == target:
        return arr.index(target)

    if target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle - 1)
    else:
        return binary_search_recursive(arr, target, middle + 1, high)
