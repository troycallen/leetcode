class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = 0
        prev = 0

        for curr, seat in enumerate(seats):
            if seat:
                if seats[prev]:
                    dist = max(dist, (curr - prev) // 2)
                else:
                    dist = max(dist, curr - prev)
                prev = curr
            
        if seats[prev]:
            dist = max(dist, len(seats) - prev - 1)
        
        return dist
            