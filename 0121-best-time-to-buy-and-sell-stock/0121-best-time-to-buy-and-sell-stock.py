class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        max_profit = 0
        curr_profit = 0

        for R in range(len(prices)):
            if prices[R] > prices[L]:
                curr_profit = prices[R] - prices[L]
                max_profit = max(max_profit, curr_profit)
            else:
                L = R
        
        return max_profit
        