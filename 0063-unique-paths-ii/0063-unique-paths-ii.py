class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Get grid dimensions
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start or end is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        # DP array: paths to each cell
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1  # Start position

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # No path through obstacle
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]  # From above
                    if j > 0:
                        dp[i][j] += dp[i][j-1]  # From left

        return dp[-1][-1]  # Paths to bottom-right