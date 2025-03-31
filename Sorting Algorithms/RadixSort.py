def find_max(arr):
    ''' for finding the maximum value from the array '''
    max_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element

def CountSort(arr , radix):
    ''' Using Count Sort as a subroutine for sorting the array as per Radix Sort '''
    
    count_array= [0]*10 # count array is length with 10 only because the range will be b/w 0 - 9
    sorted_array = [0]*len(arr)

    # couting the occurance
    for num in arr:
        digit = (num//radix) % 10
        count_array[digit]+=1

    # calculating prefix for the index
    for i in range(1 , 10):
        count_array[i]+=count_array[i-1]

    # sort array
    # starting from the last element so that it maintains the stability
    for i in reversed(arr):
        digit = ( i // radix ) % 10 
        sorted_array[count_array[digit] - 1] = i 
        count_array[digit]-=1

    print(f'array - {sorted_array} sorted , according to radix - {radix}')

    # copying the array 
    for i in range(len(arr)):
        arr[i] = sorted_array[i]

def RadixSort(arr):
    ''' sorting the array according to Radix '''

    max_num = find_max(arr)
    radix = 1

    while max_num // radix > 0:
        
        CountSort(arr , radix)
        radix*=10
    

if __name__ == '__main__':

    arr = list(map(int , input('Enter numbers with space - ').split())) 
    RadixSort(arr)
    print(f'final sorted array - {arr}')
