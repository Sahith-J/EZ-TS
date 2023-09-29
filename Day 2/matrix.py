# randomly generate 4*4 matrix
import random as r
rows=int(input("Enter no of rows:"))
cols=int(input("Enter no of columns:"))
m=[[0]*cols for i in range(rows)]
for i in range(rows):
    for j in range(rows):
        m[i][j]=r.randint(0,1)
c1,c2,c3,c4,c5,c6,c7,c8=0,0,0,0,0,0,0,0
for i in range(rows):
    for j in range(cols):
        print(m[i][j],end=" ")
    print("")

for i in range(rows):
    sum1=0
    for j in range(cols):
        sum1+=m[i][j]
    if sum1==rows:
        c1+=1
    if sum1==0:
        c5+=1

for i in range(rows):
    sum1=0
    for j in range(cols):
        sum1+=m[j][i]
    if sum1==cols:
        c2+=1
    if sum1==0:
        c6+=1

sum1 = sum(m[i][i] for i in range(rows))
if sum1 == rows:
    c3 += 1
if sum1 == 0:
    c7 += 1

sum1 = sum(m[i][rows - 1 - i] for i in range(rows))
if sum1 == cols:
    c4 += 1
if sum1 == 0:
    c8 += 1

print("1's Horizontal Count:",c1)
print("1's Vertical Count:",c2)
print("1's Left Diagonal",c3)
print("1's Right Diagonal",c4)
print("0's Horizontal Count:",c5)
print("0's Vertical Count:",c6)
print("0's Left Diagonal",c7)
print("0's Right Diagonal",c8)
