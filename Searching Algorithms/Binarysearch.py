def BinarySearch(arr , target , start , stop):
    """    Binary Search    """
    if start <= stop:
        mid = (start+stop)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return BinarySearch(arr , target , mid+1 , stop)
        else:
            return BinarySearch(arr,target , start , mid - 1)
    return -1

if __name__ == '__main__':
    arr = list(map(int , input('Enter elements with space - ').split()))
    print(BinarySearch(arr , 1 , 0 , len(arr)-1))
