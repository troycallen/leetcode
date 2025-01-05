class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap  = []

        for i in nums:
            #print("HEAP = ", min_heap)
            heapq.heappush(min_heap, i)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
            
        
        #print("final heap =", min_heap)
        return min_heap[0]