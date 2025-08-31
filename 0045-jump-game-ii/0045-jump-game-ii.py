class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_reach = 0
        max_reach = 0 
        count = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr_reach:
                count += 1
                curr_reach = max_reach
            
        return count
