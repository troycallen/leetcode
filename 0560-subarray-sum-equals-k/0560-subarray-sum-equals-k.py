class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for i in nums:
            cur_sum += i
            diff = cur_sum - k

            res += prefix_sums[diff]
            prefix_sums[cur_sum] += 1
        
        return res
            