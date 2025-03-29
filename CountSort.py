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
    for i in range(len(count_array)):
        for j in arr:
            if i == j:
                count_array[i]+=1

    # sort array
    sorted_array = []
    for i in range(len(count_array)):
        if count_array[i]!=0:
            sorted_array.extend([i] * count_array[i])

    return sorted_array

# taking user input
if __name__ == '__main__':
    arr = list(map(int , input('Enter elements with space  - ').split()))   
    print(countSort(arr))

