# Histogram pattern
l=list(map(int,input().split()))
"""
for i in range(len(l)):
    print('X '*l[i])

for i in range(1,len(l)):
    print(i,end=" ")

"""

for j in range(max(l),0,-1):
    print(f"{j:2d} | ",end="")
    for i in range(0,len(l)):
        if l[i]>=j:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
    


    