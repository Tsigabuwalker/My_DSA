class Solution:
    def smallestRangeII(self, nums, k):
        nums.sort()
        res = nums[-1] - nums[0]  # initial score
        
        for i in range(len(nums) - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i+1] - k)
            res = min(res, high - low)
        
        return res
