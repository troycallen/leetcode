from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # Sort original array
        nums.sort()
        # Make a copy and sort for the permuted array
        perm = sorted(nums)
        n = len(nums)
        i = j = res = 0
        # Use two pointers to greedily maximize greatness
        while i < n and j < n:
            if perm[j] > nums[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
