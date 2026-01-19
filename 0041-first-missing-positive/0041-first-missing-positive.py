class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # While the current number is in the valid range [1, n]
            # and it is not at its correct position (nums[i] - 1)...
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap it to its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # After sorting, the first index 'i' where nums[i] != i + 1
        # tells us that 'i + 1' is the missing number.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers 1 to n are present, the answer is n + 1
        return n + 1