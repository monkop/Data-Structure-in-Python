# solve bubble sort using python or def funtion
def bubble(arr):
    n = len(arr)

    for i in range(0,n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [99, 33 , 22 , 66, 11]
bubble(arr)
print(arr)