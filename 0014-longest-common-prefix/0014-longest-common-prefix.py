class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]

        for i in range(len(first)):
            for s in strs:
                if s[i] != first[i] or i == len(s):
                    return res
            res += s[i]
        
        return res