# Find the Max element of an array
l=list(map(int,input().split()))
def divide(n,l,r,max=0):
    if l==r:
        return n[l]
    mid=(l+r)//2
    left=divide(n,l,mid)
    right=divide(n,mid+1,r)
    return left if left>right else right 

print(divide(l,0,len(l)-1))