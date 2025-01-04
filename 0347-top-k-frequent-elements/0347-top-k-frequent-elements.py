class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # or Counter(nums)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Create heap of [-count, num] to get max heap
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, [-cnt, num])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res