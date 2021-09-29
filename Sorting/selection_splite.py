arr = input("Enter Your Array :").split()
n = len(arr)
arr1 = map(int, arr)
arr = list(arr1)

for i in range(n-1):
    minpos = i
    for j in range(i,n):
        if arr[j] < arr[minpos]:
            minpos = j

    temp = arr[i]
    arr[i] = arr[minpos]
    arr[minpos] = temp

print("Your Sorted Array :",arr)