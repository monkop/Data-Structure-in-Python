from array import *
def linearSearch(arr, n, key):
    pos = -1
    flag = 0
    for i in range(n):
        if (arr[i] == key):
            flag = 1
            pos = i
            break
    if (flag == 1):
        return flag,pos
    else:
       return flag,pos
arr = []
n = int(input("Enter Size : "))
for i in range(n):
    array = int(input("Enter Array : "))
    arr.append(array)
key = int(input("Enter Number to  search : "))
flag,pos = linearSearch(arr, n, key)

if flag == 1:
    print(f"Value found {pos+1} position")
else:
    print("Value not found")

