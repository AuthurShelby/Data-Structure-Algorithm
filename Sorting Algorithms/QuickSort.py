def quickSort(arr , start , end):
    if start < end:
        # Get the pivot index from partition
        pivotIndex = partition(arr, start, end)
        # Sort left part (before pivot)
        quickSort(arr, start, pivotIndex - 1)
        # Sort right part (after pivot)
        quickSort(arr, pivotIndex + 1, end)

def partition(arr, start, end):
    pivot = arr[end]  # Selecting the last element as pivot
    index = start - 1  # Pointer for smaller elements
    
    for i in range(start, end):
        if arr[i] <= pivot:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]  # Swap elements
    
    # Place pivot in correct position
    index += 1
    arr[index], arr[end] = arr[end], arr[index]
    
    return index  # Return final pivot position

if __name__ == '__main__':
    arr = list(map(int, input('Enter elements with spaces: ').split()))
    quickSort(arr, 0, len(arr) - 1)
    print('Sorted:', arr)
