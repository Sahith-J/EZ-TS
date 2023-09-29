# Bit Toggler
def toggleKthBit(n, k):
    return (n ^ (1 << (k-1)))


n=list(map(int,input().split()))
print( toggleKthBit(n[0] , n[1]+1))
