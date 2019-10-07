# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for index in range(cur_index, len(arr)):
            if arr[index] < arr[smallest_index]:
                arr[smallest_index], arr[index] = arr[index], arr[smallest_index]

    print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
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


# STRETCH: implement the Count Sort function below

def count_sort(arr, maximum=-1):
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
    for k in arr:
        result[count_array[k] - 1] = k

        # in case of multiple occurrence
        # insert the number in the index to the left
        count_array[k] -= 1

    return result
