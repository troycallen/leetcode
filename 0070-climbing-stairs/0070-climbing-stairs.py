class Solution:
    def climbStairs(self, n: int) -> int:
        current = 1
        prev = 1

        for i in range(n - 1):
            temp = current
            current = prev + temp
            prev = temp
        
        return current

        