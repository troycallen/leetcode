class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            print(s[i])
            substring = s[i: i + minSize]
            if len(set(substring)) <= maxLetters:
                res[substring] += 1
            
        return max(res.values()) if res else 0