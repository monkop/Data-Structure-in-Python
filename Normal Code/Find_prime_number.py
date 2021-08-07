num = int(input("enter your number : "))
count = 0

for i in range(2, (num//2+1)):

    if(num % i == 0):
        count = count + 1
        break

if (count == 0 and num != 1):
    print(" %d is a Prime Number" % num)
else:
    print(" %d is not a Prime Number" % num)
