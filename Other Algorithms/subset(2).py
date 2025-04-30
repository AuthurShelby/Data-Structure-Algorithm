def subsets(arr , ans , i , allsubs):
    if i == len(arr):
        for i in ans :
            print(i , end=' ')
        print()
        return 0 

    ans.append(arr[i])
    subsets(arr , ans , i+1 , allsubs)
    ans.pop()
    idex = 1+i
    while (idex<len(arr) and arr[idex] == arr[idex-1]):
        idex+=1
    subsets(arr , ans , idex , allsubs)

if __name__ == '__main__':
    arr = [1 ,2,2]
    ans = []
    i = 0
    allsubs = []
    subsets(arr , ans , i , allsubs)