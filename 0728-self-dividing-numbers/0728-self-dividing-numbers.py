class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result = []

        for num in range(left, right + 1):
            x = num
            ok = True

            while x > 0:
                digit = x % 10
                if digit == 0 or num % digit != 0:
                    ok = False
                    break
                x //= 10

            if ok:
                result.append(num)

        return result
