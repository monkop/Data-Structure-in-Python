def linerSearch(arr,n,key):
    pos = -1
    flag = 0
    for i in range(n):
        if (arr[i] == key):
            flag = 1
            pos = i
            break
    if flag == 1:
        return flag,pos
    else:
        return flag,pos

arr = []
n = int(input("Enter Size Of Array : "))
for i in range(n):
    array = int(input("Enter list of array : "))
    arr.append(array)
print(arr)

key = int(input("Enter Number for search : "))

flag,pos = linerSearch(arr,n,key)

if flag == 1:
    print(f"Value found {pos+1} this Position")
else:
    print("Value Not Found")