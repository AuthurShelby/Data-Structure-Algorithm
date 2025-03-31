def BubbleSort(arr):
    for _ in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

if __name__ == '__main__':
    arr = [5,4,3,2,1]
    print(BubbleSort(arr))
