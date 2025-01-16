class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if c < 0 or r < 0 or c >= COLS or r >= ROWS or (r,c) in path or board[r][c] != word[i]:
                return False
            

            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or 
            dfs(r, c + 1, i + 1) or 
            dfs(r, c - 1, i + 1))
            path.remove((r,c))

            return res
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


