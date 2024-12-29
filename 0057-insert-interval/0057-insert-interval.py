class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [intervals[0]]
        new_start, new_end = newInterval

        #print(new_start)
        

        for start,end in intervals:
            prev_start, prev_end = res[-1]
            if start < new_end and start < prev_end:
                res[-1][1] = max(new_end, prev_end)
            elif end > new_start and end > prev_start:
                res[-1][0] = min(new_start, prev_start)
            elif end < new_end and start > new_start:
                continue
            else:
                res.append([start,end])
                
        return res