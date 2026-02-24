from math import inf

class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]
        
        # dp[i][j][m]: min cost to merge stones[i..j] into m piles
        dp = [[[inf]*(k+1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i][1] = 0
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                for m in range(2, k+1):
                    for mid in range(i, j, k-1):
                        dp[i][j][m] = min(dp[i][j][m],
                                           dp[i][mid][1] + dp[mid+1][j][m-1])
                # merge k piles into 1 if possible
                if (length - 1) % (k - 1) == 0:
                    dp[i][j][1] = dp[i][j][k] + prefix[j+1] - prefix[i]
        
        return dp[0][n-1][1]