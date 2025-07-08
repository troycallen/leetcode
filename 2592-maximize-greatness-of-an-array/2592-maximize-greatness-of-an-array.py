from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        L = 0 

        greatness = 0

        for R in range(len(nums)):
            if nums[R] > nums[L]:
                greatness += 1
                L += 1
        
        return greatness
