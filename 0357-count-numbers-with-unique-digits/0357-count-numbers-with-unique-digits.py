class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 10          # for n = 1
        unique_digits = 9   # choices for first digit
        available = 9       # remaining digits

        for i in range(2, n + 1):
            unique_digits *= available
            count += unique_digits
            available -= 1

        return count
