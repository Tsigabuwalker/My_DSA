class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        
        # Edge cases
        if abs(target) > total or (target + total) % 2 == 1:
            return 0
        
        P = (target + total) // 2
        
        dp = [0] * (P + 1)
        dp[0] = 1
        
        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[P]
