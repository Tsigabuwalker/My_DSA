class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_line(start, end):
            prev1 = 0
            prev2 = 0

            for i in range(start, end):
                curr = prev1
                if prev2 + nums[i] > curr:
                    curr = prev2 + nums[i]

                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            rob_line(0, n - 1),  # exclude last house
            rob_line(1, n)       # exclude first house
        )
