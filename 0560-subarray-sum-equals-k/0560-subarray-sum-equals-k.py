class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0 : 1}

        for i in nums:
            curSum += i
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        
        return res
