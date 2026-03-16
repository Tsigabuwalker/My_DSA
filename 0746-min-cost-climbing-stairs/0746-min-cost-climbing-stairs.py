class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # dp[i] = minimum cost to reach step i
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # The top is beyond the last step, so we can end at either n-1 or n-2
        return min(dp[n-1], dp[n-2])


# Example usage:
sol = Solution()
print(sol.minCostClimbingStairs([10, 15, 20]))        # Output: 15
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # Output: 6
