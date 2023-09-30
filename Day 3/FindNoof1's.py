# Find number of set bits
n=int(input())

'''
c=0
while(n!=0):
    c+=n&1
    n=n>>1
print(c)

'''
res = 0
n=abs(n)
while n:
        n &= n - 1
        res += 1
print(res)
