arr = []
n = int(input("Enter Size : "))
for i in range(n):
    array = int(input("Enter List : "))
    arr.append(array)
print(arr)
mx = -19999999
for i in range(n):

    mx = max(mx, arr[i])
    print(mx)

