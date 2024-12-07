class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter, defaultdict

        count = Counter(s)

        non = defaultdict(int)

        for i,v in enumerate(s):
            if count[v] <= 1:
                return i
        
        return -1

