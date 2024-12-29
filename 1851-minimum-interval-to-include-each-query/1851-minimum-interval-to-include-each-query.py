class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res = {}
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                # only adding intervals (left < query) that are valid
                l, r = intervals[i]     # get the left and right value
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            # right value of smallest interval
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            res[query] = min_heap[0][0] if min_heap else -1
        
        return [res[query] for query in queries]