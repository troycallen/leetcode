class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []

        for pos, val in lights:
            start = pos - val
            end = pos + val + 1
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        currB, maxB, pos = 0, 0, 0

        print(events)

        for position, change in events:
            print(position,change)
            currB += change
            if currB > maxB:
                currB = maxB
                pos = position
        
        return pos
            