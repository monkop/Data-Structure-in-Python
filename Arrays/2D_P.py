def linerSearch(arr, matrix, row, col, key):
    pos = -1
    flag = 0
    for i in range(row):
        for j in range(col):
            if(matrix[i][j] == key):
                flag = 1
                pos = i, j
                break
    if flag == 1:
        return flag, pos
    else:
        return flag, pos
        
        if flag == 1:
            return flag, pos
        else:
            return flag, pos


matrix = []
row = int(input("Enter Size of row : "))
col = int(input("Enter Size of columns : "))

for i in range(row):
    arr = []
    for j in range(col):
        arr.append(int(input()))
    matrix.append(arr)

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()

key = int(input("Enter number for Search : "))
flag, pos = linerSearch(arr, matrix, row, col, key)

if flag == 1:
    print(" Value is find ")
else:
    print(" Value is not found ")
