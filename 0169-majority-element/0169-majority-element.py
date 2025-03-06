class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums) // 2
        cnts = defaultdict(int)

        for i in nums:
            cnts[i] += 1
            if cnts[i] > k:
                return i
        