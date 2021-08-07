row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))

matrix = []
print("Enter the entries row : ")

for i in range(row):
    arr = []
    for j in range(col):
        arr.append(int(input("Enter number : ")))
    matrix.append(arr)

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print() 