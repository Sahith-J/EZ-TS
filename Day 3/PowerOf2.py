# determine whether a number is power of 2
n=int(input())
if n>0:
    if n&(n-1):
        print("No")
    else:
        print("Yes")
else:
    print("No")

