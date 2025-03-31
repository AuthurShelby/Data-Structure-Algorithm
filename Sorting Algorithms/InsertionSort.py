def InsertionSort(arr):
    # range starting from 1 because the first of the array is always sorted
    for i in range(1 , len(arr)):
        # Key is set as the current element
        key = arr[i]
        # prev stores the preves elements index
        prev = i-1
        # the while runs only if the prev index is  greater or equal to zero 
        # and prev element is greater than key
        while prev >=0 and arr[prev] > key:
            # only if the condition is true then the prev element is being right shifted
            arr[prev+1] = arr[prev]
            # then prev index is being decremented
            prev -= 1
            # and the loop run until any of the condition becomes false 
        
        # Now we got out of the loop the prev will be the element were the comparison has become false
        # So the key value will be placed at the correct position just after the prev
        arr[prev+1] = key
    
    return arr

# main part
if __name__ == '__main__':
    # enter the list of elements
    ARR = list(map(int , input('Enter the elements with space: ').split()))
    RESULT = InsertionSort(ARR)
    print('Sorted Array - ' , RESULT)
