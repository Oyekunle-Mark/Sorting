def merge(arrA, arrB):
    """Helper function to merge two array while sorting them in the process

    Arguments:
        arrA {list} -- the left array
        arrB {list} -- the right array

    Returns:
        list -- the merged and sorted array
    """
    merged_arr = []
    # start checking from the start of both arrays
    i, j = 0, 0

    # while both arrays are not empty
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    # while arrA is not empty
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1

    # while arrB is not empty
    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


def merge_sort(arr):
    """Implementation of the merge sort algorithm

    Arguments:
        arr {list} -- array to be sorted

    Returns:
        list -- sorted list
    """
    # base case
    if len(arr) < 2:
        return arr

    # recursive case
    midpoint = len(arr) // 2
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
