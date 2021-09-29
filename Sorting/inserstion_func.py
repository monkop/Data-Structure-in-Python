# solve insertion sort using python or def function

def insertion(arr):
    n = len(arr)

    for i in range(1,n):
        temp = arr[i]
    j = i-1
    while j>=0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j-=1
        arr[j+1] = temp

i = [22,55,33,44,11]
insertion(i)
print(i)