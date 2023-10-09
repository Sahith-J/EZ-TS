"""
def SQRT(x):
    left,right=0,n+1
    while left<right:
        mid=left+(right-left)//2
        if mid*mid>x:
            right=mid
        else:
            left=mid+1
    return left-1
n=int(input())
print(SQRT(n))
"""
"""
x=int(input())
si=0
li=x
floor=-1
while si<=li:
    mid=(si+li)//2
    if mid*mid==x:
        floor=mid
        break
    elif mid*mid<x:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)
"""
# Recursion now
def sqrt(n,si,li,floor):
    if n<0:
        return -1
    if n==1:
        return 1
    if si<=li:
        mid=(si+li)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            floor=mid
            return sqrt(n,mid+1,li,floor)
        else:
            return sqrt(n,si,mid-1,floor)
    return floor

x=int(input())
si=0
li=x//2
floor=-1
print(sqrt(x,si,li,floor))


    
    
    
