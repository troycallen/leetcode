class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        curr_reach = 0
        count = 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, nums[i] + i)
            
            if i == curr_reach:
                curr_reach = max_reach
                count += 1
 

        return count
            

