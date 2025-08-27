class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
       
        prev = 0
        max_dist = 0

        for curr, seat in enumerate(seats):
            if seat:
                if seats[prev]:
                    max_dist = max(max_dist, (curr - prev) // 2)
                else:
                    max_dist = max(max_dist, (curr- prev))
                
                prev = curr
            
        
        if seats[prev]:
            max_dist = max(max_dist, len(seats) - prev - 1)
        
        return max_dist
 
 
