def print_matrix(mat):
    for row in mat:
        print(row)
def longest_sequence(mat, s1, s2, row, col):
    s = ""
    while row>0 and col>0:
        if s1[row-1]==s2[col-1]:
            s=s1[row-1]+s
            row-=1
            col-=1
        elif mat[row-1][col]>mat[row][col-1]:
            row-=1
        else:
            col-=1
    print("Longest Common Subsequence:",s)
def LCS(s1, s2):
    row, col = len(s1)+1, len(s2)+1
    mat = [[None]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if i==0 or j == 0:
                mat[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    print_matrix(mat)
    longest_sequence(mat,s1,s2,row-1,col-1)
    return mat[row-1][col-1]
s1 = input()
s2 = input()
#s2=s1[::-1]
answer = LCS(s1, s2)
print("My answer is: ",answer)