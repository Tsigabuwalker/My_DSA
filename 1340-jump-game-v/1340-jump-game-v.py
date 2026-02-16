class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [-1] * n
        
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            
            max_visit = 1  # count itself
            
            # check left
            for x in range(1, d + 1):
                left = i - x
                if left < 0 or arr[left] >= arr[i]:
                    break
                max_visit = max(max_visit, 1 + dfs(left))
            
            # check right
            for x in range(1, d + 1):
                right = i + x
                if right >= n or arr[right] >= arr[i]:
                    break
                max_visit = max(max_visit, 1 + dfs(right))
            
            dp[i] = max_visit
            return dp[i]
        
        return max(dfs(i) for i in range(n))
