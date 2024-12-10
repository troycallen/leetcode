import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        min_heap = []

        for i in intervals:
            if min_heap and min_heap[0] <= i[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, i[1])
        
        return len(min_heap)