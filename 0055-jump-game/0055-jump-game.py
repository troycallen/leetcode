class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        goal = len(nums) - 1

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(i + nums[i], max_reach)
            
            
            if max_reach >= goal:
                return True
        
        return False