class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        F = 0
        for i in range(n):
            F += i * nums[i]

        max_F = F

        for k in range(1, n):
            F = F + total - n * nums[-k]  # recurrence formula
            if F > max_F:
                max_F = F

        return max_F
