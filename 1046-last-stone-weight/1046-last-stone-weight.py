class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = 0

        max_heap = [-s for s in stones]

        print(max_heap)
        #print(max_heap)
        heapq.heapify(max_heap)
        print(max_heap)

        while len(max_heap) > 1:
                x = -heapq.heappop(max_heap)
                y = -heapq.heappop(max_heap)
                if x != y:
                    heapq.heappush(max_heap, (y - x))
                
                print(max_heap)
        
        if max_heap:
            stone = -max_heap[0]
        return stone
                
