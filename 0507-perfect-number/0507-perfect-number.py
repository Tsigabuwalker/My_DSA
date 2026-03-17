import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1 is not a perfect number
        if num == 1:
            return False

        total = 1  # 1 is always a divisor
        # Loop up to sqrt(num) to find divisors efficiently
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                total += i
                if i != num // i:  # avoid double-counting when num is a square
                    total += num // i

        return total == num


# Example usage:
sol = Solution()
print(sol.checkPerfectNumber(28))  # True
print(sol.checkPerfectNumber(7))   # False
