class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        res = []

        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        
        for i in heap:
            res.append(i[1])
        
        return res
        

        
        

        


            