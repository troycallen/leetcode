class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        count = min(w1, w2)
        longer = max(w1, w2)
        res = ""

        for i in range(longer):
            if w1 > w2:
                res += word1[i]
                if count > 0:
                    res += word2[i]
                count -= 1
            else:
                if count > 0:
                    res += word1[i]
                
                res += word2[i]
                count -= 1

        
        return res
                

