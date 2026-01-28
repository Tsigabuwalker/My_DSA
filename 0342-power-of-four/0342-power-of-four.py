class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (
            n > 0 and
            (n & (n - 1)) == 0 and   # power of two
            (n & 0x55555555) != 0   # 1-bit in even position
        )
