class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        nums = sorted((nums[i], i) for i in range(len(nums)))
        print(nums)
        heapLeft = []
        heapRight = []

        minDiff = 99999999999

        for i in range(len(nums)):
            val, index = nums[i]

            heapq.heappush(heapLeft, (index, val))
            heapq.heappush(heapRight, (-index, val))

            while heapLeft and heapLeft[0][0] + x <= index:
                minDiff = min(minDiff, val - heapq.heappop(heapLeft)[1])

            while heapRight and heapRight[0][0] + x <= -index:
                minDiff = min(minDiff, val - heapq.heappop(heapRight)[1])
            
        return minDiff

