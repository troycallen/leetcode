class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        res = ""

        for i in range(len(first)):
            for s in strs:
                #print(s[i])
                if i == len(s) or s[i] != first[i]:
                    return res
            res += s[i]
        
        return res

            
