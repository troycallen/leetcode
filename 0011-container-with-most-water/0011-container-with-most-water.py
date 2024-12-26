class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0

        l = 0 
        r = len(height) - 1

        while l < r:
            curr_area = abs(l - r) * min(height[l], height[r])

            if curr_area > most_water:
                r -= 1
            else:
                l += 1
            

            most_water = max(curr_area, most_water)
        return most_water

            
