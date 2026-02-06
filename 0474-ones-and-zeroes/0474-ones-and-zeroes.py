class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            
            # Update dp table from bottom to top to avoid reuse
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        
        return dp[m][n]
