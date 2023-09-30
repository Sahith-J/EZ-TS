# Power of 4
n=int(input())
if n>0 and n&(n-1)==0 and n%2==1: 
    print("Yes")
else:
    print("No")