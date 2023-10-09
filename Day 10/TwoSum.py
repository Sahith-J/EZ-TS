# find pairs that sum to a target value

l=list(map(int,input().split()))
target=int(input())
left=0
right=len(l)-1
while left<=right:
    if l[left]+l[right]<target:
        left+=1
    elif l[left]+l[right]>target:
        right-=1
    else:
        print([left,right])
        break
    



    