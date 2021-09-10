import numpy as np
arr = []
n = int(input())
for i in range(n):
    n1  = int(input())
    arr.append(n1)
print(np.array(arr)[::-1])
