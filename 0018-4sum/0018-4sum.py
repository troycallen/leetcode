class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l = j + 1
                r = len(nums) - 1
                
                while l < r:
                    four_sum = a + nums[j] + nums[l] + nums[r]
                    
                    if four_sum < target:
                        l += 1
                    elif four_sum > target:
                        r -= 1

                    else:
                        res.append([a, nums[j], nums[l], nums[r]])
                        r -=1 
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                        while l < r and nums[r] == nums[r+1]:
                            r -=1 
        return res
                 