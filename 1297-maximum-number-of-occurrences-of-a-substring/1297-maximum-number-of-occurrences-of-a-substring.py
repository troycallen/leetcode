class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            substr = (s[i:i + minSize])
            #counts[substr] += 1
            if len(set(substr)) <= maxLetters:
                counts[substr] += 1
            print(substr)
        
        return max(counts.values()) if counts else 0

        



        
        
