arr = input("Enter Your Array : ").split()
n = len(arr)
arr1 = map(int, arr)
arr2 = list(arr1)
for i in range(0,n):
    for j in range(n-1-i):
        if arr2[j] > arr2[j+1]:
            temp = arr2[j]
            arr2[j] = arr2[j+1]
            arr2[j+1] = temp
print("sorted array : ",arr2)