class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        Map1={i:[] for i in range(n)}
        for i,j in edges:
            Map1[i].append(j)
            Map1[j].append(i)
        q=[source]
        vis=set()
        vis.add(source)
        while q:
            a=q.pop(0)
            for i in Map1[a]:
                if i==destination:
                    return True
                if i not in vis:
                    q.append(i)
                    vis.add(i)
        return False