class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""

        for i in range(len(first)):
            for s in strs:
                if i == len(s) or s[i] != first[i]:
                    return res

            res += first[i]
        
        return res
        

            
