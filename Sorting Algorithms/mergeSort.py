def Merge(arr , start , mid , end):
    ''' Merging of the array '''
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    # i and j pointer will starting from 0
    i = j = 0
    # k can vary so stored as start value
    k = start
    
    # Merge elements from both halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # mergin the value and incrementing the pointers
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            # mergin the value and incrementing the pointers
            j+=1
            k+=1
        
    # Copy remaining elements of right list (if any)
    if i == len(left):
        # storing all the values of the sorted 'right' list
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

    # # Copy remaining elements of left list (if any)
    if j == len(right):
        while i < len(left):
            # storing all the values of the sorted 'left' list
            arr[k] = left[i]
            k+=1
            i+=1

def MergeSort(arr , start , end):
    ''' Merge with Sort '''
    if start < end:
        # mid value
        mid  = start+ (end - start)//2
        # for sorting the left side
        MergeSort(arr , start , mid)
        # for sorting the right side
        MergeSort(arr , mid+1 , end)
        # Mergin the left - right
        Merge(arr , start , mid , end)

# Execution 
if __name__ == '__main__':

    arr = list(map(int , input('Enter a list with spaces :- ').split()))
    # calling the MergeSort function
    MergeSort(arr , 0 , len(arr)-1)
    # giving the result of a sorted array
    print(arr)
