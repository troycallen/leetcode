class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = 0 
        dist = 0 

        for curr, seat in enumerate(seats):
            if seat: # if a seat with val 1 is found
                if seats[prev]:
                    # if we also have a seat to the left
                    dist = max(dist, (curr - prev) // 2)
                else:
                    dist = max(dist, curr - prev)
                
                prev = curr

        
        if seats[prev]:
            dist = max(dist, len(seats) - prev - 1)
        
        return dist
 
