arr = []
n = int(input("Enter Size of array :"))
for i in range(n):
    n1  = int(input("Enter Your Array : "))
    arr.append(n1)

for i in range(n-1):
    minpos = i
    for j in range(i,n):
        if arr[j] < arr[minpos]:
            minpos = j

    temp = arr[i]
    arr[i] = arr[minpos]
    arr[minpos] = temp

print("Your Sorted Array :",arr)
