class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSub = 0
        maxSub = -10000

        for i in nums:
            if curSub < 0:
                curSub = 0
            curSub += i
            maxSub = max(curSub, maxSub)
        
        return maxSub
        

        