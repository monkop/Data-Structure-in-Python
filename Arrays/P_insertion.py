arr = []
n = int(input("Enter Size of arrays : "))
for i in range(n):
    array = int(input("Enter list of arrays : "))
    arr.append(array)
print("Your Unsorted array",arr)

for i in range(1,n):
    temp = arr[i]
    j = i-1
    while j>=0 and arr[j] > temp:
       arr[j+1] = arr[j]
       j -= 1
       arr[j+1] = temp
print(arr)
