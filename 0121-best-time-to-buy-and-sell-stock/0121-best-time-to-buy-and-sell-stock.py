class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        L = 0 

        for R in range(len(prices)):
            curr_profit = prices[R] - prices[L]
            max_profit = max(curr_profit, max_profit)
            if prices[R] > prices[L]:
                continue
            else:
                L = R
            
        return max_profit
