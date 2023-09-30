def Move(n):
    if n==1:
        return 1
    else:
        return 2*Move(n-1)+1
n=int(input())
print(Move(n))