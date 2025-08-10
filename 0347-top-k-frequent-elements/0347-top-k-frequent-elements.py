class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        counts = Counter(nums)


        print(counts)

        for num, cnt in counts.items():
            heapq.heappush(heap, (-cnt, num))
    

        for i in range(k):
            cnt, num = heapq.heappop(heap)
            res.append(num)
        
        return res

        
