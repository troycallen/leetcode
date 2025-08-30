class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0 
        pairs = 0
        res = 0

        for r in range(len(nums)):
            pairs += freq[nums[r]]
            freq[nums[r]] += 1
            
            while pairs >= k:
                res += len(nums) - r
                out = nums[l]
                freq[out] -= 1
                pairs -= freq[out]
                l += 1
            
        return res

