class Solution:
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        max_pair = 0
        
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]
            max_pair = max(max_pair, pair_sum)
        
        return max_pair

