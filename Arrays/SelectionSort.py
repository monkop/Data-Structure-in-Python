arr = []
n = int(input("Size : "))
for i in range(n):
    array = int(input("Enter List : "))
    arr.append(array)
print(arr)

for i in range(n-1):
        minpos = i

        for j in range(i,n):
            if arr[j] < arr[minpos]:
                minpos = j

        temp = arr[i]
        arr[i] = arr[minpos]
        arr[minpos] = temp
print("Your Sorted Array is : ",arr )