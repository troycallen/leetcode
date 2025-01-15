class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        

        L = 0
        R = len(height) - 1
        water = 0

        left_max = height[L]
        right_max = height[R]

        while L < R:
            if left_max < right_max:
                L += 1
                left_max = max(height[L], left_max)
                water += left_max - height[L]
            else:
                R -= 1
                right_max = max(height[R], right_max)
                water += right_max - height[R]

        return water                
            
