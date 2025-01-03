class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        
        rows = len(grid)
        cols = len(grid[0])

        num_islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                # out of beounds and water check
                return 

            grid[row][col] = '0'

            dfs(row -1, col)
            dfs(row +1 , col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r,c)

        return num_islands

