class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0

        for num in range(left, right + 1):
            count = 0
            x = num
            while x > 0:
                if x & 1:
                    count += 1
                x >>= 1

            if count in primes:
                ans += 1

        return ans
