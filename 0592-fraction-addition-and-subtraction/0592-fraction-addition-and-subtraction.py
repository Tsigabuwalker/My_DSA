class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math

        num, den = 0, 1  # running result
        i = 0
        n = len(expression)

        while i < n:
            sign = 1
            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            # read numerator
            numerator = 0
            while i < n and expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1
            numerator *= sign

            i += 1  # skip '/'

            # read denominator
            denominator = 0
            while i < n and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1

            # add fractions
            num = num * denominator + numerator * den
            den = den * denominator

            # reduce
            g = math.gcd(abs(num), den)
            num //= g
            den //= g

        return f"{num}/{den}"
