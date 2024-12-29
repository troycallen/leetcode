class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]

        for start,end in intervals:
            prev_end = res[-1][1]
            if start < prev_end:
                res[-1][1] = min(prev_end, end)
            else:
                res.append([start,end])
        
        return len(intervals) - len(res)
            