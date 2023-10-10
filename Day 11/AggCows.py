#Aggressive Cows
n=int(input())
k=int(input())
stalls=list(map(int,input().split()))
#stalls.sort()

#True --> l=mid+1
#False --> r=mid-1
def solve(n,k,stalls):
    stalls.sort()
    si=0
    li=stalls[-1]-stalls[0]
    res=0
    while si<=li:
        mid=(si+li)//2
        if isValid(n,k,stalls,mid):
            res=mid
            si=mid+1
        else: 
            li=mid-1
    return res
def isValid(n,k,stalls,mid):
    prevcow=stalls[0]
    count=1
    for i in stalls:
        if i-prevcow>=mid:
            count+=1
            prevcow=i
    return True if k==count else False

print(solve(n,k,stalls))

