def InterpolationSearch(arr , key):
    # setting the low as 0 
    # also high as length of arr -1 for getting the last element 
    low , high = 0 , len(arr)-1

    # checking if the low is less than or equal to high 
    # also if the key is between or equal to the low / high 
    while low<=high and key >= arr[low] and key <= arr[high]:
        # if the low and high index are equal 
        if low == high:
            # if the low/high  index is the value of key / target
            if arr[low] == key:
                return low 
            # else to return -1 if the element is not the key 
            return -1
        # The probable position(pp) is being found with using the interpolation equation
        pos = low+(((high - low) * key - arr[low]) //(arr[high] - arr[low]))

        # If the arr[pp] is the key 
        if arr[pos] == key:
            return pos
        # if the arr[pos] is less than key value
        elif arr[pos] < key:
            low=pos+1
        
        # if the arr[pos] is greater than key value
        else:
            high = pos -1 
    
    # -1 if the element is not found
    return -1

# main part
if __name__ == '__main__':
    # enter the list of elements
    ARR = list(map(int , input('Enter the elements with space: ').split()))
    # target/key value
    TAR = int(input('Enter the element to be found: '))
    # result value
    RESULT = InterpolationSearch(ARR , TAR)
    # checking if the result is returned as -1 
    if RESULT!=-1:
        print(f'The element being found at {RESULT}!')
    else:
        print('Element Not found!')