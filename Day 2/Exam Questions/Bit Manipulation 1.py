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
