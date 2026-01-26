class Solution:
    def minimumTotal(self, triangle):
        # Start with the last row
        dp = triangle[-1].copy()
        
        # Move from second-last row to top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]

# Example usage
sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # Output: 11
print(sol.minimumTotal([[-10]]))                         # Output: -10
