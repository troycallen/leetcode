class Solution:
    def climbStairs(self, n: int) -> int:
        current = 1
        prev = 1

        for i in range(n - 1):
            temp = prev
            prev = prev + current
            current = temp
        
        return prev

        