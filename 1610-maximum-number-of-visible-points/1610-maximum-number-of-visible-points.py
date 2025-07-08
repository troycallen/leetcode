class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same = 0
        angles = []

        for px, py in points:
            if [px, py] == location:
                same += 1
                continue
            dx, dy = px - location[0], py - location[1]

            theta = math.degrees(math.atan2(dy, dx))

            if theta < 0:
                theta += 360
            angles.append(theta)
        angles.sort()

        n = len(angles)

        angles += [a + 360 for a in angles]

        max_visible = 0
        left = 0

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)
        
        return max_visible + same
