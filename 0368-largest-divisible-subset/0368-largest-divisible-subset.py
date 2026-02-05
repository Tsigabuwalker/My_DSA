class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        
        max_size = 0
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            
            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i
        
        result = []
        curr = max_idx
        while curr != -1:
            result.append(nums[curr])
            curr = parent[curr]
            
        return result[::-1]