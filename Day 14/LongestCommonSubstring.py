s1=input()
s2=input()
"""
"""
res1=[]
res2=[]
for i in range(len(s1)):
    for j in range(i,len(s1)):
        res1.append(s1[i:j+1])
for i in range(len(s2)):
    for j in range(i,len(s2)):
        res2.append(s2[i:j+1])
max1=0
res3=[]
for i in res1:
    for j in res2:
        if i==j:
            res3.append(i)
            l=len(i)
            if l>max1:
                max1=l
                res=i
print(res)

"""
Map={}
for i in range(len(res3)-1):
    Map[len(res3[i])]=res3[i]
for key,values in Map.items():
    if key==max((Map.keys())):
        print(Map[key])
"""
