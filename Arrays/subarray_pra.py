arr = []
n = int(input("Enter Size : "))
for i in range(n):
    array = int(input("Enter List : "))
    arr.append(array)
print(arr)


for i in range(n):
    curr = 0
    for j in range(0,n):
        curr += arr[j]
        print(curr)