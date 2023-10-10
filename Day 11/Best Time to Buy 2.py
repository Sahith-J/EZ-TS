class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_p += prices[i] - prices[i-1]
        return max_p

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy=prices[0]
        for i in prices:
            if i<buy:
                buy=i
            elif i-buy>0:
                max_p+=i-buy
                buy=i
        return max_p

