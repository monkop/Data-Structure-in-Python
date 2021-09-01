import numpy as np

arr = []
a = int(input("Size of array:"))
for i in range(a):
    arr.append(int(input("Element:")))
arr = np.array(arr)
print(np.floor(arr))