class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odd = 0
        l, m = 0, 0

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            
            if odd > k:
                l = m+1
                m = l
                odd -= 1

            if odd == k:
                while not nums[m] % 2:
                    m += 1
                res += (m - l) + 1

        return res