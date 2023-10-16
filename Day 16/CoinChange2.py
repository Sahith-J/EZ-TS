# Said to do on our own 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nDP = [0] * (amount + 1)
            nDP[0] = 1

            for a in range(1, amount + 1):
                nDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nDP[a] += nDP[a - coins[i]]
            dp = nDP
        return dp[amount]  