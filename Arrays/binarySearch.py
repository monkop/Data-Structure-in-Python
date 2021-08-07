def binarySearch(arr,n,key):
    s = 0
    e = n-1
    flag = 0
    while(s<=n and flag == 0):
        mid = (s+e)//2

        if (arr[mid] == key):
            
            flag = 1
            pos = mid+1

        elif (arr[mid] > key):
            e = mid - 1
        elif (arr[mid] < key):
            s = mid +1
    if flag == 1:
        print("Value is found")
    else:
        print("Value not found")

arr = []
n = int(input("Enter Array Size : "))

for i in range(n):
    array = int(input("Enter Arrays : "))
    arr.append (array)
print(arr)

key = int(input("Enter no for search : "))

binarySearch(arr,n,key)