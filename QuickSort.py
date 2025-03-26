def quickSort(arr , start , end):
    if start < end:
        # Taking out the pivot index from the partition 
        pivotIndex = partition(arr , start , end)
        # Sorting the left side
        quickSort(arr , start , pivotIndex-1)
        # Sorting the right side 
        quickSort(arr , pivotIndex+1 , end)

# partition for making the list the as left side that is less
# than the pivot number and right is the numbers greater 
# than the pivot 
def partition(arr , start ,end):
    Index = start - 1 
    PIVOT = arr[end] # Taking out the last element of the array as the pivot element
    for i in range(start , end):
        if arr[i] <= PIVOT:
            Index+=1
            arr[i] , arr[Index] = arr[Index] , arr[i]

    Index+=1
    arr[Index] , arr[end] = arr[end] , arr[Index]
    return Index


if __name__ == '__main__':
    arr = list(map(int , input('Enter elements with spaces - ').split()))
    quickSort(arr , 0 , len(arr)-1)
    print('Sorted - ' , arr)