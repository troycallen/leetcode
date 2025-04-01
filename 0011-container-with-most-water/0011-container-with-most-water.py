class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0 
        R = len(height) - 1

        max_area = 0

        while L < R:
            curr_area = min(height[L], height[R]) * (R - L)
            max_area = max(max_area, curr_area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_area




            
