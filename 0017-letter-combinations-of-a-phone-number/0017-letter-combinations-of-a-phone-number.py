class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = ""
        digit_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        def dfs(i, cur_str):
            if i >= len(digits):
                res.append(cur_str)
                return 
            
            for char in digit_map[digits[i]]:
                dfs(i + 1, cur_str + char)
            
        if digits:
            dfs(0, cur)
        return res
                
