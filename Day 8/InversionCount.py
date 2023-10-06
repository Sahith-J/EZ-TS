#Merge Sort using Inversion Count
# Inversion Count -- > 
# if the elements are not in order then increase count 
# no of pairs such that elements are not in order is called Inversion Count
# l[i]>[j] while i<j
# time is O(n^2)


l=list(map(int,input().split()))
count=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            count+=1
print(count)
