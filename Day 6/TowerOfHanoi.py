def toh(n,source,aux,dest):
    if n>0:
        toh(n-1,source,dest,aux)
        print(source,dest)
        toh(n-1,aux,source,dest)

n=int(input())
toh(n,'A','B','C')


