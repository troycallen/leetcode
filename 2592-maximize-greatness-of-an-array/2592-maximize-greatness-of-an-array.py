class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        j = 0 
        
        for i in range(n):
            if nums[j] < nums[i]:
                res += 1
                j += 1
        
        return res