class Solution:
    def brightestPosition(self, lights: list[list[int]]) -> int:
        # Initialize event list
        events = []
        
        # Convert each light into two events: start of brightness and end of brightness
        for position, radius in lights:
            events.append((position - radius, 1))   # entering brightness
            events.append((position + radius + 1, -1))  # leaving brightness
        
        print(events)
        # Sort events by coordinate
        events.sort()
        
        # Initialize brightness, maximum brightness, and result position
        brightness = 0
        maxBrightness = 0
        resultPosition = 0
        
        # Sweep through events
        for coordinate, delta in events:
            
            # Update brightness
            brightness += delta
            
            # Check for maximum brightness and update result
            if brightness > maxBrightness:
                maxBrightness = brightness
                resultPosition = coordinate
        
        return resultPosition