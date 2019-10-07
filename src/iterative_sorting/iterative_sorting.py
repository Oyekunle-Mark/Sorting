# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    """An implementation of the selection sort algorithm

    Arguments:
        arr {list} -- the list to be sorted

    Returns:
        list -- the sorted list
    """
    arr_len = len(arr)

    for i in range(0, arr_len - 1):
        smallest_index = i

        for index in range(i, arr_len):
            if arr[index] < arr[smallest_index]:
                arr[smallest_index], arr[index] = arr[index], arr[smallest_index]

    return arr


def bubble_sort(arr):
    """An implementation of the bubble sort algorithm

    Arguments:
        arr {list} -- the list to be sorted

    Returns:
        list -- the sorted list
    """
    swapped = False

    for index in range(0, len(arr)):
        for cur_index in range(index, len(arr) - 1):
            if arr[index] > arr[cur_index + 1]:
                arr[index], arr[cur_index +
                                1] = arr[cur_index + 1], arr[index]
                swapped = True

        if not swapped:
            return arr

    return arr


def count_sort(arr, maximum=-1):
    """Implementation of the count sort algorithm
    https://www.programiz.com/dsa/counting-sort
    https://www.geeksforgeeks.org/counting-sort/
    These links help make sense of the algorithm

    Arguments:
        arr {list} -- the list to be sorted

    Keyword Arguments:
        maximum {int} -- [description] (default: {-1})

    Returns:
        list -- a new sorted list
    """
    # return back an empty array
    if len(arr) == 0:
        return []

    # will hold the sorted arr
    result = [0] * len(arr)

    # initialize a count array of greater in length than the maximum element in array by 1
    high = max(arr)
    count_array = [0 for i in range(high+1)]

    # count the occurrence of each number in the array
    for i in arr:
        # this sort does not work with negative numbers
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"

        count_array[i] += 1

    # Modify the count array such that each element at each index
    # stores the sum of previous counts
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j-1]

    # Find the index of each element of the original array in count array.
    # This gives the cumulative count.
    # Place the element at the index calculated.
    for i in arr:
        result[count_array[i] - 1] = i

        # in case of multiple occurrence
        # insert the number in the index to the left
        count_array[i] -= 1

    return result
