class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = 0
        max_dist = 0

        for i, seat in enumerate(seats):
            if seat:
                if seats[prev]:
                    max_dist = max(max_dist, (i - prev) // 2)
                else:
                    max_dist = max(max_dist, (i - prev))
                
                prev = i

        if seats[prev]:
            max_dist = max(max_dist, len(seats) - 1 - prev)
        
        return max_dist
 
