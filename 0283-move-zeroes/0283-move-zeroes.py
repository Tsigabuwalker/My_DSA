class Solution:
    def moveZeroes(self, nums):
        k = 0  # position for next non-zero

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # Fill remaining positions with zero
        for i in range(k, len(nums)):
            nums[i] = 0
