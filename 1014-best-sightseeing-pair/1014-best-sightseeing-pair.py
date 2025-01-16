class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr_best = 0  # Best score found so far
        prev_best = values[0] + 0  # Best value[i] + i seen so far
        
        for i in range(1, len(values)):
            # For current index i, use it as j in the pair
            curr_best = max(curr_best, prev_best + values[i] - i)
            
            # Then consider current index i as potential future i
            prev_best = max(prev_best, values[i] + i)
            
        return curr_best
