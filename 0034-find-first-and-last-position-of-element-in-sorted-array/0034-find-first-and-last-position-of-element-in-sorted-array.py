class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L = self.binarySearch(nums, target, True)
        R = self.binarySearch(nums, target, False)

        return [L, R]
    
    def binarySearch(self, nums, target, leftBias):
        L = 0
        R = len(nums) - 1
        res = -1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                res = mid
                if leftBias:
                    R = mid - 1
                else:
                    L = mid + 1
        return res




        


        


        

        
        

        