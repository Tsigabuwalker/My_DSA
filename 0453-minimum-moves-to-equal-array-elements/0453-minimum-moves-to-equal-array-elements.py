class Solution:
    def minMoves(self, nums):
        n = len(nums)
        min_val = nums[0]
        total = 0
        
        # Find min
        for num in nums:
            if num < min_val:
                min_val = num
        
        # Sum differences
        for num in nums:
            total += num - min_val
        
        return total
