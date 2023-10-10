# Fractional Knapsack 
weights=list(map(int,input().split()))
prices=list(map(int,input().split()))
capacity=int(input())
per_ratio=[]
for i in range(0,len(prices)):
    per_ratio.append(prices[i]/weights[i])

l=list(zip(weights,prices,per_ratio))
l.sort(key=lambda x:x[2],reverse=True)
print(l)

i=0
profitmax=0
while capacity!=0:
    if l[i][0]<=capacity:
        capacity-=l[i][0]
        profitmax+=l[i][2]*l[i][0]
    elif l[i][0]>capacity:
        profitmax+=capacity*l[i][2]
        break
        
    i+=1

print(profitmax)