# find the way of biggest number of 3 element

a = int(input("Enter Your First Number : "))
b = int(input("Enter Your Second Number : "))
c = int(input("enter Your third Number : "))

if a > b and a>c:
    print("A is greater then b and c")
elif b>c and b>a:
    print("b is greater then a and c")
elif c>a and c>b:
    print("c is greater then a and b")
else:
    print("all three value is equal")