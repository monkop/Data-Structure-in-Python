arr = []
n = int(input("Enter Size of array : "))
for i in range(n):
    array = int(input("Enter list of array : "))
    arr.append(array)
print("Your Unsorted arrays",arr)

for i in range(n):
    for j in range(n-1-i):
        if (arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print("Your Sorted Array",arr)