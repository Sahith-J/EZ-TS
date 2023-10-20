class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        vis=set()
        ans=[]
        def dfs(start,res):
            res.append(start)
            if start==n-1:
                ans.append(res[:])
            else:
                for i in graph[start]:
                    if i not in res:
                        vis.add(i)
                        dfs(i,res)
                        vis.remove(i)
            res.pop()
        dfs(0,[])
        return ans