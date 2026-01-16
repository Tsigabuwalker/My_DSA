class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # If no pivot is found, the array is in descending order (e.g., [3,2,1])
        # Just reverse it to get the smallest order [1,2,3]
        if pivot == -1:
            nums.reverse()
            return
        
        # Step 2: Find the smallest element on the right larger than pivot
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                # Step 3: Swap them
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break
        
        # Step 4: Reverse the sub-array to the right of pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1