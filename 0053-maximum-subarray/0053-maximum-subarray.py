class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSub = 0

        for i in nums:
            if curSub < 0:
                curSub = 0
            curSub += i
            maxSub = max(maxSub,curSub)
        return maxSub

        