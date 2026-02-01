class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        nums.sort()
        half = (len(nums) + 1) // 2
        
        # Split into small and large halves
        small = nums[:half]
        large = nums[half:]
        
        # Fill odd and even indices from the back
        # Even indices (0, 2, 4...) get smaller numbers
        # Odd indices (1, 3, 5...) get larger numbers
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = small.pop()
            else:
                nums[i] = large.pop()