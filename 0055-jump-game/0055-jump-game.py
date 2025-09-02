class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i >= max_reach:
                return False 

        return True