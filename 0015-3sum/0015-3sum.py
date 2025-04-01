class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            #print(a)
            # if the first number is greater than 0 we can just break since rest will be > 0
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l- 1] and l < r:
                        l += 1
        return res
