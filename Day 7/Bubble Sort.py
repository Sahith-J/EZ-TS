#Bubble sort

l=list(map(int,input().split()))
n=len(l)
'''
for i in range(0,len(n)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

'''
flag=False
for i in range(1,n):
    for j in range(n-1):
        if l[j]>l[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
if flag==False:
    print(l)
    flag=False
else:
    print(l)

# Total no of swap is n*(n-1)//2

    
    




