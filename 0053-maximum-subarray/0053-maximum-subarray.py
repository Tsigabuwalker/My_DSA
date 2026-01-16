class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize with the first element
        max_so_far = nums[0]
        current_max = nums[0]
        
        for i in range(1, len(nums)):
            # Kadane's logic: extend the sequence or start over
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far