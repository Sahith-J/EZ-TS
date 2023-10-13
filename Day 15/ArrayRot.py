l=list(map(int,input().split()))
k=int(input())
#[1,2,3,4,5]
#k = 3
# 3,4,5,1,2
"""
#Logic 3 I didn't make
if len(l)==0 or k==0:
    print("")
if k>=len(l):
    k=k%len(l)
a=len(l)-k
l[:]=l[a:]+l[:a]
print(l)
"""
"""
# Logic 2 I didn't make
n=len(l)
for i in range(k):
    temp=l[-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=temp
print(l)

"""

"""
# Logic 1 I didnt make
for i in range(k):
    l.insert(0,l.pop())
print(l)

"""
"""
#Logic 4
for i in range(k-1):
    x = l.pop(0) 
    l.append(x)
print(l)

"""
"""
#Logic 3
k %= len(l)
for _ in range(k):
    temp = l[-1]
    for i in range(len(l) - 1, 0, -1):
        l[i] = l[i - 1]    
    l[0] = temp    
print(l)
"""
"""
#Logic 2 
k=k%len(nums)
l[:] = l[-k:] + l[:-k]
print(l)

"""
"""
# Logic 1
temp=l[k:]
l=l[:k]
l=temp+l
print(l)
"""




