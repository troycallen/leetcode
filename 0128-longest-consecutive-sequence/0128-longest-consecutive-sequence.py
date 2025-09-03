class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for i in numSet:
            if (i - 1) in numSet:
                continue
            length = 1
            while (i + 1) in numSet:
                i += 1
                length += 1
            
            longest = max(longest, length)
        
        return longest

        