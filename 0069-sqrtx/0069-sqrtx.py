class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 
        r = x
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)

            if m ** 2 < x:
                l = m + 1
                res = m
            elif m ** 2 > x:
                r = m - 1
            else:
                return m
            
        return res