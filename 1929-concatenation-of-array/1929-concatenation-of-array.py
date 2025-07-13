class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        curr = 0

        for i in range(n*2):
            if i >= n:
                res.append(nums[curr])
                curr += 1
            else:

                res.append(nums[i])
        
        return res
