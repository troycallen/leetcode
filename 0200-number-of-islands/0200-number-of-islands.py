class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        
        ROWS = len(grid)
        COLS = len(grid[0])

        islands = 0

        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands
