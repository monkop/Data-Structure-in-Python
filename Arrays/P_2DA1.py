row , col = int(input("Enter Size Of 2d arrays"))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(row):         
    a =[]
    for j in range(col):      
         a.append(int(input()))
    matrix.append(a)
  

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print()