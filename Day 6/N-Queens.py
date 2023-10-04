class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res=[]
        col=list()
        posDiag=list() 
        negDiag=list()
        board=[["."]*n for i in range(n)]
        def backtrack(r=0):
            if r==n:
                res.append(["".join(row)for row in board])
                return res
            for c in range(n):
                if c in col or (r+c) in posDiag or r-c in negDiag:
                    continue

                col.append(c)
                posDiag.append(r+c)
                negDiag.append(r-c)
                board[r][c]='Q'
                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."
        backtrack()
        return res

            
            
        
