def ps(arr , ans , i):
    if i == len(arr):
        for k in ans:
            print(k,end = ' ')
        print()
        return 0
    ans.append(arr[i])
    ps(arr , ans , i+1)
    ans.pop()
    ps(arr, ans , i+1)

if __name__ == '__main__':
    arr = [1 ,2 ,3]
    ans = []
    i = 0
    ps(arr , ans , i)