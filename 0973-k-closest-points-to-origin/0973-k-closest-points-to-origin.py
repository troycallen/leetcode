class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        for point in points:
            #print(point)
            x = point[0]
            y = point[1]
            dist = (x * x) + (y * y)
            heapq.heappush(min_heap, (dist, (x,y)))
        
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res

 