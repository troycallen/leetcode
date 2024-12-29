class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Tracks furthest index we can reach
    
        for i in range(len(nums)):
            if i > max_reach:  # Can't reach current position
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
            if max_reach >= len(nums) - 1:  # Can reach end
                return True
                
        return True