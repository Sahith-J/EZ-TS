# print the lonely integers in an array
nums=list(map(int,input().split()))
res=0
for n in nums:
    res=res^n
print(res)
