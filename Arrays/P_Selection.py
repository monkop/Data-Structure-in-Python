arr = []
n = int(input("Enter Your Size of arrays : "))
for i in range(n):
    array = int(input("Enter list of arrays : "))
    arr.append(array)
print("Your Unsorted Arrays ", arr)

for i in range(n-1):
    minpos = i
    for j in range(i,n):
        
        if (arr[j] < arr[minpos]):
            minpos = j

            temp = arr[i]
            arr[i] = arr[j+1]
            arr[j+1] = temp

print("your sorted array", arr)