class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []

        res.append(intervals[0])

        for start, end in intervals[1:]:
            prev_end = res[-1][1]

            if prev_end >= start:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start,end])

        return res
