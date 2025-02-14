class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in prev:
                return prev[diff], ind
        
            prev[val] = ind
        
        