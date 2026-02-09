class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        total_xor = 0
        for num in nums:
            total_xor ^= num

        # If XOR is 0, Alice wins immediately
        if total_xor == 0:
            return True

        # Otherwise, Alice wins if the length of nums is even
        return len(nums) % 2 == 0
