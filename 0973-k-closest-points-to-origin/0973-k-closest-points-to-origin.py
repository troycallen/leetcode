class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        for point in points:
            #print(point)
            x = point[0]
            y = point[1]
            dist = (x * x) + (y * y)
            min_heap.append([dist,x,y])
        
        heapq.heapify(min_heap)
        for i in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        return res

 