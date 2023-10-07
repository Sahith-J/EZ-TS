# Find Sum of array elements
def divide(n,l,r):
    if l==r:
        return n[l]
    mid=(l+r)//2
    left=divide(n,l,mid)
    right=divide(n,mid+1,r)
    return left+right

l=list(map(int,input().split()))
print(divide(l,0,len(l)-1))

