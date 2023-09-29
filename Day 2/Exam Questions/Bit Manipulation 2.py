# Bit Toggler
def toggleKthBit(n, k):
    return (n ^ (1 << (k)))


n=list(map(int,input().split()))
print( toggleKthBit(n[0] , n[1]))
