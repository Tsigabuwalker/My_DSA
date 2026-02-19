class Solution:
    def maxSumDivThree(self, nums):
        dp = [0, -1, -1]   # -1 means not reachable
        
        for num in nums:
            temp = dp[:]   # copy previous state
            
            for r in range(3):
                if temp[r] != -1:  # only valid states
                    new_sum = temp[r] + num
                    new_r = new_sum % 3
                    dp[new_r] = max(dp[new_r], new_sum)
        
        return dp[0]
