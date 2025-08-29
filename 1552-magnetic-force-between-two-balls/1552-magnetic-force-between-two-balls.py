class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        L = 0
        R = position[-1] - position[0]
        force = 0

        while L <= R:
            mid = (L + R) // 2

            last_pos = position[0]
            balls = 1

            for i in range(len(position)):
                if position[i] - last_pos >= mid:
                    last_pos = position[i]
                    balls += 1
                
            if balls >= m:
                force = mid
                L = mid + 1
            else:
                R = mid - 1
        
        return force
            

            