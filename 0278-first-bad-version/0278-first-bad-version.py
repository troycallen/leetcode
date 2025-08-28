# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        L = 0 
        R = n

        while L < R:
            mid = (L + R) // 2
            
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1

        return L 
        