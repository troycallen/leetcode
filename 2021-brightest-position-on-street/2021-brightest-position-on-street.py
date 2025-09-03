class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []
        currB = 0
        maxB = 0
        bestPos = 0

        for pos, val in lights:
            start = pos - val
            end = pos + val + 1
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()

        for position, change in events:
            currB += change

            if currB > maxB:
                currB = maxB
                bestPos = position
        
        return bestPos

        
            