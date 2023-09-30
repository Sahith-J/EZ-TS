# Find what element is missing in the range of 0 to n 

n=int(input())
x=list(map(int,input().split()))    
sum1=0
for i in range(len(x)):
    sum1=sum1+x[i]
sum2=(n*(n+1))//2
if sum1==sum2:
    print(0)
else:
    print(sum2-sum1)



"""
nums=list(map(int,input().split()))
res = len(nums)
for i in range(len(nums)):
    res += i - nums[i]
print(res)
"""

"""
# only works for input in ascending order
n=int(input())
x=0
nums=list(map(int,input().split()))
for i in range (len(nums)):
    x=x^i
for i in range (len(nums)-1):
    x=x^nums[i]
print(x)


"""
