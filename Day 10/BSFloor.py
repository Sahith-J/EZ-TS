def BSFloor(l,target):
    start=0
    end=len(l)-1
    floor=-1
    #ceil=float('inf')
    while start<=end:
        mid=(start+end)//2
        if l[mid]==target:
            return l[mid]
        elif l[mid]>target:
            ceil=l[mid]
            end=mid-1
        else:
            floor=l[mid]
            start=mid+1
    return floor

def BSCeil(l,target):
    start=0
    end=len(l)-1
    floor=-1
    #ceil=float('inf')
    while start<=end:
        mid=(start+end)//2
        if l[mid]==target:
            return l[mid]
        elif l[mid]>target:
            ceil=l[mid]
            end=mid-1
        else:
            floor=l[mid]
            start=mid+1
    return ceil

l=list(map(int,input().split()))
target=int(input())
print(BSFloor(l,target))
print(BSCeil(l,target))

    