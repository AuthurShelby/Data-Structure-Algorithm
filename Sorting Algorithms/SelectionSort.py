# selection sort
arr = list(map(int , input('Enter a list of elements with space : ').split()))
n = len(arr)
for i in range(n):
    for j in range(i+1 , n):
        if arr[i] > arr[j]:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
print(arr)
