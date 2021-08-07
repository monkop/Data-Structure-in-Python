from array import *
arr = []
n = int(input("Enter your number : "))

for i in range(0, n):
    array = int(input(""))
    arr.append(array)

max = arr[0]
for i in range(n):
    if(arr[i] > max):
        max = arr[i]

min = arr[0]
for i in range(n):
    if(arr[i] < min):
        min = arr[i]
print(f"Your Max Value {max}, And min Value is {min}")
