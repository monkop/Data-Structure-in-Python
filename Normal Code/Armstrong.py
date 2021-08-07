num = int(input("Enter Your Number : "))
orin = num 
sum = 0

while num>0:
    sum = sum + (num%10) * (num%10) * (num%10)
    num = num // 10
   

if orin == sum:
    print("Number Is Armstrong ")
else:
    print("Number is not Armstrong")