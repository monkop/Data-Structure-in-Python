from array import *


def linerSearch(arr, matrix, row, col, key):
    pos = -1
    flag = 0
    for i in range(row):
        for j in range(col):
            if (matrix[i][j] == key):
                flag = 1
                pos = i, j
                break

    if(flag == 1):
        return flag, pos
    else:
        return flag, pos

        if(flag == 1):
            return flag, pos
        else:
            return flag, pos


row = int(input("Enter size of row : "))
col = int(input("Enter Size of colnmns : "))

matrix = []
print("Enter the entries of row : ")

for i in range(row):
    arr = []
    for j in range(col):
        arr.append(int(input("")))
    matrix.append(arr)
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()

key = int(input("Enter number for search : "))

flag, pos = linerSearch(arr, matrix, row, col, key)

if flag == 1:
    print("Value is found  position")
else:
    print("Value is not find ")
