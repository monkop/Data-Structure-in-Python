arr = []
n = int(input("Size : "))

for i in range(n):
    array = int(input("Enter List Of array : "))
    arr.append(array)
print(f"Your Array {arr}")

for i in range(n-1):
    for j in range(n-1-i):
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("Sorted Array is :",arr)
