n = int(input())
for i in range(0,n+1):
    print(" "*(n-i)+"* "*i)
for j in range(n,0,-1):
    print(" "*(n-j)+"* "*j)
