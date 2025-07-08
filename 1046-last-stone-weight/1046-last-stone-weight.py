class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = 0
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, y - x)
            

        if max_heap:
            return -max_heap[0]
        else:
            return 0

            
                
