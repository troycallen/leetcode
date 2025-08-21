class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                               # maps value to its index
        for i, x in enumerate(nums):            # iterate through numbers with indices
            need = target - x                   # value needed to reach target
            if need in seen:                    # if we've seen the complement, return indices
                return [seen[need], i]
            seen[x] = i                         # otherwise record current value's index
        return []