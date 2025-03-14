class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        [-4, -1, -1, 0, 1, 2]

        for i,a in enumerate(nums):
            # It will always be positive solution so we can break
            if a > 0:
                break
            
            # dont use the same element twice
            if i > 0 and a == nums[i -1]:
                continue
            
            # need l to be 2nd potential element in the triplet
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                
                elif three_sum > 0:
                    r -= 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
        return res
                

