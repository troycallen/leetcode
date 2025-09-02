class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        sortedNums = sorted((val, i) for i ,val in enumerate(nums))
        heapLeft = []
        heapRight = []
        minDiff = float('inf')

        for val, index in sortedNums:
            heapq.heappush(heapLeft, (index, val))
            heapq.heappush(heapRight, (-index, val))

            while heapLeft and heapLeft[0][0] + x <= index:
                minDiff = min(minDiff, val - heapq.heappop(heapLeft)[1])

            while heapRight and heapRight[0][0] + x <= -index:
                minDiff = min(minDiff, val - heapq.heappop(heapRight)[1])
        
        
        return minDiff

        