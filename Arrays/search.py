def search(arr, n, find_val):

    for i in range(0, n):
        if (arr[i] == find_val):
            return i
    return -1


arr = ["10", "23", "45", "34", "66"]
find_val = "66"
n = len(arr)

result = search(arr, n, find_val)

if (result == -1):
    print("Element is not present in array")
else:
    print("Element present in array",result)
