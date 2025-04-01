class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 

        L = 0
        R = len(height) - 1
        left_max = height[L]
        right_max = height[R]

        water = 0

        while L < R:
            if height[L] < height[R]:
                left_max = max(height[L], left_max)
                water += left_max - height[L]
                L += 1
            else:
                right_max = max(height[R], right_max)
                water += right_max - height[R]
                R -= 1
        return water

        
            
