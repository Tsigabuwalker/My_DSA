class Solution:
    def repeatedNTimes(self, nums):
        n = len(nums)
        
        for k in range(1, 4):  # check distance 1, 2, 3
            for i in range(n - k):
                if nums[i] == nums[i + k]:
                    return nums[i]