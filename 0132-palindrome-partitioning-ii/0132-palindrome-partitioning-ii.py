class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Palindrome table
        isPal = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
        
        # Step 2: DP for minimum cuts
        dp = [0] * n
        
        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(1, i + 1):
                    if isPal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        
        return dp[-1]
