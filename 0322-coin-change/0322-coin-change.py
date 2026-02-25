class Solution:
    def coinChange(self, coins, amount):
        # Initialize DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Build up the dp table
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If impossible, return -1
        return dp[amount] if dp[amount] != float('inf') else -1