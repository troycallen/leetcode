class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            substring = s[i: i + minSize]

            if len(set(substring)) <= maxLetters:
                counts[substring] += 1
            
            
        if counts:
            return max(counts.values())
        else:
            return 0