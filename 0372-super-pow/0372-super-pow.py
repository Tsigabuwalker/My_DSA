class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337

        def mod_pow(x, n):
            res = 1
            x %= MOD
            while n > 0:
                if n & 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n >>= 1
            return res

        result = 1
        for digit in b:
            result = mod_pow(result, 10) * mod_pow(a, digit) % MOD

        return result
