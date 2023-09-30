def toh(n,s,a,d):
    if n==0:
        return
    toh(n-1,s,d,a)
    print("disk",n,"from",s,"to",d)
    toh(n-1,a,s,d)
n=int(input())
s,a,d=input().split()
toh(n,s,a,d)