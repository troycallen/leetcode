class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        max_prof = 0

        for R in range(len(prices)):
            if prices[R] > prices[L]:
                curr_prof = prices[R] - prices[L]
                max_prof = max(max_prof, curr_prof)
            else:
                L = R
            
        return max_prof