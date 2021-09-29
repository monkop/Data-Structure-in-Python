# solve insertion sort using python or simple input method

arr = []
n = int(input("Enter Size of array :"))
for i in range(n):
    n1 = int(input("Enter list of array :"))
    arr.append(n1)

for i in range(1,n):
    temp = arr[i]
    j = i-1
    while j>=0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j-=1
        arr[j+1] = temp
print("Your Sorted Array : ",arr)


