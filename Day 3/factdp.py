def DPfact(N):
    arr={}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
        arr[N] = 1
    else:
        factorial = N*DPfact(N - 1)
        arr[N] = factorial
    return factorial
    
num=int(input(""))
print(DPfact(num))