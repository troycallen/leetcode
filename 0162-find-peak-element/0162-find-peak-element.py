class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1


        while L <= R:
            mid = L + ((R - L)// 2)
            if mid < len(nums) - 1 and nums[mid] < nums[mid+1]:
                L = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                R = mid - 1
            else:
                return mid
        


