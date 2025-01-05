import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []

        for start,end in intervals:
            if min_heap and end > min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)
        
        return len(min_heap)

        