#profits=list(map(int,input().split()))
#weights=list(map(int,input().split()))
'''
def knapsack(wt, val, W, n): 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
    if wt[n-1] <= W: 
        t[n][W] = max( val[n-1] + knapsack( wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W:  
        t[n][W] = knapsack(wt, val, W, n-1) 
        return t[n][W] 
  
profit = [60, 100, 120] 
weight = [10, 20, 30] 
W = 50
n = len(profit)  
t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
print(knapsack(weight, profit, W, n)) 
'''


def knapsack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)
print(knapsack(W, weight, profit, n))

