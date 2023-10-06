# Quick Sort
# elements less than pivot <pivot <elements greater than pivot

def qsorting(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[j],l[i]=l[i],l[j]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def func(n,start,end):
    if start<end:
        pi=qsorting(n,start,end)
        func(n,start,pi-1)
        func(n,pi+1,end)

n=list(map(int,input().split()))
pivot=len(n)//2
start=0
end=len(n)-1
func(n,start,end)
print(n)

# Complexity of qsorting function is O(n) 
# But Complexity of fun quick ( recursion) depends on depth of recursion tree 
# worst case is O(n^2) ( the depth is n )
# best and average is O(nlogn) ( the depth is logn )
