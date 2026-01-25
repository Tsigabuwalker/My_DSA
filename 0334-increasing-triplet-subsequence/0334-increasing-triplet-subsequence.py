class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                # num > first and num > second
                return True

        return False
