class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        length = 2
        while length <= n:
            left = 1
            while left + length - 1 <= n:
                right = left + length - 1
                dp[left][right] = 10**9  # large number
                
                x = left
                while x <= right:
                    cost = x + max(dp[left][x - 1], dp[x + 1][right])
                    if cost < dp[left][right]:
                        dp[left][right] = cost
                    x += 1
                
                left += 1
            length += 1
        
        return dp[1][n]
