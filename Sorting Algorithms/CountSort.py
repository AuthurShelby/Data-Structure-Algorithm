# finding the maximum 
def find_max(arr):

    max_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            
    return max_element

def countSort(arr):
    max_element = find_max(arr)
    # creating count array 
    count_array = [0]*(max_element+1)
    # count_array = [0*i for i in range(max+1)]

    # filling the count array
    for num in arr:
        count_array[num]+=1

    # calculating the prefix 
    for i in range(1,len(count_array)):
        count_array[i] += count_array[i-1]

    # sort array
    # starting from the last element so that it maintains the stability 
    sorted_array = [0]*len(arr)
    for num in reversed(arr):
        sorted_array[count_array[num]-1] = num
        count_array[num]-=1

    return sorted_array

# taking user input
if __name__ == '__main__':
    arr = list(map(int , input('Enter elements with space  - ').split()))   
    print('Sorted Array - ' , countSort(arr))

