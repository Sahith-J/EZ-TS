# 1 --> (n//2,n-1)
# 2 --> (i-1,j+1) 
# always decrement row by 1 and increase column by 1
# if j==n: then make j=0
# if i<0 then make i=n-1
# if i<0 and j==n: then make i=0 and j=n-2
# if sq[i][j]: then make i=i+1 and j=j-2
def magic(n):
    matrix=[[0]*n for i in range(n)] 
    def fill(i,j,num):
        if num > n * n:
            return matrix

        if i < 0 and j == n:
            i = 0
            j = n - 2
        else:
            if i < 0:
                i = n - 1
            if j == n:
                j = 0

        if matrix[i][j]:
            i = i + 1
            j = j - 2
            return fill(i,j,num)
        matrix[i][j] = num
        return fill(i - 1, j + 1, num + 1)
    return fill(n//2,n-1,1)
n=int(input())
print(magic(n))

'''
def magic(i,j):
    if num>n*n:
        return 
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if matrix[i][j]:
        i=i+1
        j=j-2
    matrix[i][j]=num
    num+=1
    i=i-1
    j=j+1
    magic(i,j)

'''
'''
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if matrix[i][j]:
        i=i+1
        j=j-2
        continue
    matrix[i][j]=num
    num+=1
    i=i-1
    j=j+1

'''



