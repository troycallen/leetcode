class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = len(nums) - 1

        while L < R:
            if nums[L] == 0:
                nums[L] = nums[R]
                nums[R] = 0
                R -= 1
            L += 1
        
