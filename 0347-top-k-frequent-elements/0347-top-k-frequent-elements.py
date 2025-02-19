class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        count = Counter(nums)

        print(count)

        for i in count.keys():
            heapq.heappush(heap, [count[i], i])
            if len(heap) > k:
                heapq.heappop(heap)
       

        print(heap)

        for i in heap:
            res.append(i[1])
        
        return res