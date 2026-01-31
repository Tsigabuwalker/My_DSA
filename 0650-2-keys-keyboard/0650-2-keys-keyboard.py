class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        steps = 0
        d = 2

        while n > 1:
            while n % d == 0:
                steps += d
                n //= d
            d += 1

        return steps
