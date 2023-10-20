class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def dfs(num):
            if num in visit:
                return
            visit.add(num)
            for key in rooms[num]:
                dfs(key)
        dfs(0)
        return len(visit) == len(rooms)
