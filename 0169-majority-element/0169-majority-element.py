class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums)

        print(counts)
        for i,v in counts.items():
            if v > (n / 2):
                return i
        
