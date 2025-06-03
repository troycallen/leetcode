class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        n = len(nums)

        for num,cnt in counts.items():
            if cnt > (n / 3):
                res.append(num)
        
        return res