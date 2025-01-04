class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0

        for R in range(len(prices)):
            if prices[L] < prices[R]:
                curr_profit = prices[R] - prices[L]  
                max_profit = max(curr_profit, max_profit)
            else:
                L = R   
            
        
        return max_profit

            
