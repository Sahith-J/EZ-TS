# Selection Sort
l=list(map(int,input().split()))
n=len(l)
for i in range(n-1):
    mini =i
    for j in range(i+1,n):
        if l[j]<l[mini]:
            mini=j
    l[i],l[mini]=l[mini],l[i]

print(l)


# Bubble Sort can be optimized but Selection sort cannot be optimized for average and best cases 
# In case of average and best cases , Bubble Sort is better than Selection Sort
# In case of worst cases, both are O(n^2) time complexity

