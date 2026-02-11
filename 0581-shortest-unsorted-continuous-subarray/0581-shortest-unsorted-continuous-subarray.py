class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        l, r = -1, -2
        max_val = nums[0]
        min_val = nums[n-1]
        
        for i in range(n):
            max_val = max(max_val, nums[i])
            if nums[i] < max_val:
                r = i
                
            j = n - 1 - i
            min_val = min(min_val, nums[j])
            if nums[j] > min_val:
                l = j
                
        return r - l + 1