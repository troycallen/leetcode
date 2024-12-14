class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0    # current depth
        max_depth = 0  # maximum depth seen
        
        for char in s:
            if char == '(':
                count += 1
                max_depth = max(max_depth, count)
            elif char == ')':
                count -= 1
                
        return max_depth
                
