# solve insertion sort using python or map , split function

arr = input("Enter Your list :").split()
n = len(arr)
arr1 = map(int, arr)
arr2 = list(arr1)

for i in range(1,n):
    temp = arr2[i]
    j = i-1
    while j>=0 and arr2[j] > temp:
        arr2[j+1] = arr2[j]

        j-=1
        arr2[j+1] = temp

print("Your Sorted Array : ",arr2)
