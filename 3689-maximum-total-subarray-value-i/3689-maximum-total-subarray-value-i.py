class Solution:
    def maxTotalValue(self, nums, k):
        min_val = nums[0]
        max_val = nums[0]
        
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        
        return k * (max_val - min_val)
