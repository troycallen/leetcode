class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_power(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x = x / 2
                else:
                    x =3 * x + 1
                steps += 1
            
            return steps

        res = []
        for i in range(lo, hi + 1):
            power = get_power(i)
            res.append((power, i))
        
        res.sort()
        return res[k - 1][1]