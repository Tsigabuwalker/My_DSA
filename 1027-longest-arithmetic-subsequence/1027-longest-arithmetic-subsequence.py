class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[i][diff])
        
        return res