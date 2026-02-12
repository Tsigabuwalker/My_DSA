class NumArray:
    def __init__(self, nums: list[int]):
        # Build prefix sum array
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Use prefix sums to calculate range sum in O(1)
        return self.prefix[right+1] - self.prefix[left]
