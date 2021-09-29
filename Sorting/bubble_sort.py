arr = []
n = int(input("Enter size of array :")) #this input ask for our array size
for i in range(n):                       
    n1 = int(input("Enter Array : "))
    arr.append(n1)
print("Your Array : ",arr) #for Showing Your actual array
for i in range(n):

    for j in range(n-1-i):
        if arr[j] > arr[j+1]:

            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp 

print("Your Sorted Array Is : ",arr)