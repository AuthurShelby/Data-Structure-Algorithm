# Linear search / Sequential search 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where it's found
    return -1  # Return -1 if not found

if __name__ == "__main__":
    arr = list(map(int , input('Enter a list of numbers with space - ').split()))
    target = int(input("Enter the number to search: "))

    result = linear_search(arr, target)
    # checks if we found the target or not 
    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found in the list.")
