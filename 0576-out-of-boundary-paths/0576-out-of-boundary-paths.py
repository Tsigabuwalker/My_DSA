class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        
        # dp[i][j] = ways to be at cell (i, j)
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        
        result = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if dp[i][j] > 0:
                        for dx, dy in directions:
                            ni, nj = i + dx, j + dy
                            
                            if ni < 0 or ni >= m or nj < 0 or nj >= n:
                                result = (result + dp[i][j]) % MOD
                            else:
                                new_dp[ni][nj] = (new_dp[ni][nj] + dp[i][j]) % MOD
            
            dp = new_dp
        
        return result
