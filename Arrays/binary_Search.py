def binarySearch(arr,n,key):
    i = 0
    j = n - 1
    flag = 0
    while i<j and flag == 0:
        mid = (i+j)//2
        if arr[mid] == key:
            flag = 1
            pos = mid+1
        elif arr[mid] > key:
            j = mid-1
        elif arr[mid] < key:
            i = mid +1

    if flag == 1:
        print("Number found at",pos)
    else:
        print("Number not found ")

arr = []
n = int(input("Enter Size of array : "))
for i in range(n):
    array = int(input("Enter list of array : "))
    arr.append(array)

print("Your Array",arr)
key = int(input("Enter value of search : "))
binarySearch(arr,n,key)

