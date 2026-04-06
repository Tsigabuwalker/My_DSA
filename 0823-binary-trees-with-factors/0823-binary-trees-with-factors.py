class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        
        dp = {}
        
        for i in range(len(arr)):
            x = arr[i]
            dp[x] = 1  # single node tree
            
            for j in range(i):
                a = arr[j]
                
                if x % a == 0:
                    b = x // a
                    
                    if b in dp:
                        dp[x] += dp[a] * dp[b]
                        dp[x] %= MOD
        
        return sum(dp.values()) % MOD