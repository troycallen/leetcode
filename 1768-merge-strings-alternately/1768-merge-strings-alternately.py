class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        res = ""
        i = 0
        j = 0 

        while n and m:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
            n -= 1
            m -= 1
        
        if n > 0:
            res += word1[i:]
        if m > 0:
            res += word2[j:]
        
        return res
