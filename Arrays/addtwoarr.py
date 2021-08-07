arr = []
n = int(input("Enter Size : "))
for i in range(n):
    array = int(input("Enter List : "))
    arr.append(array)
print("Your First Array",arr)

a = []
n = int(input("Enter Size : "))
for i in range(n):
    ar = int(input("Enter List : "))
    a.append(ar)
print("Your Second Array", a)

c= a+arr
print("added two Arrays",c)