# DFS Code
edges=list(map(int,input().split()))
n=int(input())
start=int(input())
Map1={i:[] for i in range(n)}
    for i,j in edges:
        Map1[i].append(j)
        Map1[j].append(i)
    q=[start]
    vis=set()
    vis.add(source)
def dfs(start,vis):
    vis.add(start)
    for i in d[start]:
        if i not in vis:
            dfs(i,vis)