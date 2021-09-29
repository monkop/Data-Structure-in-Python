# solve bubble sort using python or map , split function
arr = input("Enter Your Array : ").split()
n = len(arr)
arr1 = map(int, arr)
listofint = list(arr1)
for i in range(0,n):
    for j in range(n-1-i):
        if listofint[j] > listofint[j+1]:
            temp = listofint[j]
            listofint[j] = listofint[j+1]
            listofint[j+1] = temp
print("sorted array : ",listofint)