class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L = 0 
        R = len(nums) - 1

        while L <= R:
            m = L + ((R - L) // 2)
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]

            leftSize = m - 1 if nums[m - 1] == nums[m] else m
            if leftSize % 2 :
                R = m - 1
            else:
                L = m + 1

