class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        goal = len(nums) - 1

        for i in range(len(nums)):
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

            if maxReach >= goal:
                return True
        
        return False



        