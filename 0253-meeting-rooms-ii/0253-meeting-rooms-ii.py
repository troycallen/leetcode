class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()

        for start,end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)