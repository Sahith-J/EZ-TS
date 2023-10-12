def generate_substrings(s1):
    def backtrack(start, path):
        res1.append(''.join(path))
        for i in range(start, len(s1)):
            path.append(s1[i])
            backtrack(i + 1, path)
            path.pop()
    res1 = []
    backtrack(0, [])
    return res1
s1=input()
s2=input()
"""
"""
res1=generate_substrings(s1)
res2=generate_substrings(s2)
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
