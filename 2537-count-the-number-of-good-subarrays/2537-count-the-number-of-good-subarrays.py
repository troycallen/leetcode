class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        pairs = 0
        res = 0

        for r in range(len(nums)):
            num = nums[r]
            pairs += freq[num]
            freq[num] += 1
            
            while pairs >= k:
                res += len(nums) - r
                remove = nums[l]
                freq[remove] -= 1
                pairs -= freq[remove]
                l += 1
        return res

