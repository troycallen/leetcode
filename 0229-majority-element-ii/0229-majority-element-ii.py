class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counts = Counter(nums)

        n = len(nums)
        for i, v in counts.items():
            if v > (n / 3):
                res.append(i)
        
        return res