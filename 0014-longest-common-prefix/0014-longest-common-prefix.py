class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]

        #flower
        # f 0
        # l 1
        # o 2
        # w 3

        for i in range(len(first)):
            for s in strs[1:]:
                if i == len(s) or s[i] != first[i]:
                    return res
            res += first[i]
        return res
            