class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        profit = 0
        curr_profit = 0

        for R in range(1, len(prices)):
            if prices[L] < prices[R]:
                curr_profit = prices[R] - prices[L]
            else:
                L = R
            profit = max(profit, curr_profit)
        
        return profit