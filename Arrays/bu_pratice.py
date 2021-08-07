arr = []
n = int(input("Enter size of array : "))
for i in range(n):
    array = int(input("Enter list of array : "))
    arr.append(array)

print(f"Your Unsorted Array {arr}")

for i in range(0,n):
    for j in range(n-1-i):
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            print(arr)
print("Your Sorted array is : ", arr)