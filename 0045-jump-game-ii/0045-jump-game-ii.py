class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_reach = 0
        max_reach = 0
        res = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            #res += 1

            if i == curr_reach:
                res += 1
                curr_reach = max_reach
                
            
        return res