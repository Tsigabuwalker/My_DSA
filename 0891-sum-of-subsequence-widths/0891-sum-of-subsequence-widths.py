class Solution:
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        # Precompute powers of 2 modulo MOD
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        result = 0
        for i in range(n):
            result = (result + nums[i] * (pow2[i] - pow2[n-1-i])) % MOD
        
        return result
