class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0
        while n:
            if n & (n - 1) == 0:
                ops += 1
                break
            if n & 1 == 0:
                n >>= 1
            else:
                if (n & 2) and n != 3:
                    n += 1
                else:
                    n -= 1
                ops += 1
        return ops