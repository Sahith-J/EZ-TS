class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return source==destination
        Map1={i:[] for i in range(n)}
        for i,j in edges:
            Map1[i].append(j)
            Map1[j].append(i)
        vis=set()
        def dfs(start,vis):
            vis.add(start)
            if start==destination:
                return True
            for i in Map1[start]:
                if i not in vis:
                    if dfs(i,vis):
                        return True
            return False
        return dfs(source,vis)
        