class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        max_ops = 0
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                max_ops = max(max_ops, i // 3 + 1)
            seen.add(nums[i])
            
        return max_ops