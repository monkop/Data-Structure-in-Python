import numpy as np
def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

arr = []
n = int(input())
for i in range(n):
    n1 = int(input())
    arr.append(n1)
l1 = len(arr)
ans = _sum(arr)
print(np.array(arr))
print(np.array(ans))