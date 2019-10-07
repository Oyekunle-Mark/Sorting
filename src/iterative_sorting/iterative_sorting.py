# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for index in range(cur_index, len(arr)):
            # TO-DO: swap
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

    return arr
