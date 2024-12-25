class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        counts = Counter(nums)

        return heapq.nlargest(k, counts.keys(), counts.get)
        
        
