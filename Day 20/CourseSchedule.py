class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Map1 = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            Map1[c].append(pre)
        vis = set()
        def dfs(c):
            if c in vis:
                return False
            if Map1[c] == []:
                return True
            vis.add(c)
            for i in Map1[c]:
                    if not dfs(i):
                        return False
            vis.remove(c)
            Map1[c]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        
