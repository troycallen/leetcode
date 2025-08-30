class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L = 0
        R = len(height) - 1
        area = 0

        left_max = height[L]
        right_max = height[R]

        while L < R:
            if height[L] < height[R]:
                L += 1
                left_max = max(left_max, height[L])
                area += left_max - height[L]
            else:
                R -= 1
                right_max = max(right_max, height[R])
                area += right_max - height[R]
        
        return area

            
