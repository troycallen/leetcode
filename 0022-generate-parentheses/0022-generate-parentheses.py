class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res  = []

        def backtrack(open_n, closed_n, s):
            if open_n == n and closed_n == n:
                res.append(s)
                return
            
            if open_n < n:
                backtrack(open_n + 1, closed_n, s + "(")
            
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, s + ")")
            
        
        backtrack(0, 0, "")
        return res



