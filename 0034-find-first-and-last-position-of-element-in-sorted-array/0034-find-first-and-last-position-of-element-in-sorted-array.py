class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target, False)
        return [l, r]

    def binarySearch(self, nums, target, search_left):
        L = 0
        R = len(nums) - 1
        res = -1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                res = mid
                if search_left:
                    R = mid - 1
                else:
                    L = mid + 1
        return res


        

        
        

        