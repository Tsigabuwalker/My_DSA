class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start or end is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Initialize DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # Fill first column
        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        
        # Fill first row
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# Example usage
sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # Output: 2
print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))              # Output: 1
