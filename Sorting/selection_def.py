def selection(arr):
    n = len(arr)

    for i in range(n-1):
        minpos = i
        for j in range(i,n):
            if arr[j] < arr[minpos]:
                minpos = j

    temp = arr[i]
    arr[i] = arr[minpos]
    arr[minpos] = temp


arr = [44,11,33,55,22]
selection(arr)
print(arr)