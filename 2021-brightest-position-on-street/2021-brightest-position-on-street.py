class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []

        for position, rangeVal in lights:
            start = position - rangeVal
            end = position + rangeVal + 1
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        currBrightness = 0
        maxBrightness = 0
        bestPos = 0

        for pos, change in events:
            print(pos, change)

            currBrightness += change
            if currBrightness > maxBrightness:
                currBrightness = maxBrightness
                bestPos = pos
        return bestPos