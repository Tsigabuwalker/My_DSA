class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        
        # Step 1: Flip negative numbers
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        
        # Step 2: If k is still left
        nums.sort()
        
        # Step 3: If k is odd, flip smallest element
        if k % 2 == 1:
            nums[0] = -nums[0]
        
        return sum(nums)