class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num):
            plus = num.find('+')
            real = int(num[:plus])
            imag = int(num[plus + 1:-1])
            return real, imag

        a, b = parse(num1)
        c, d = parse(num2)

        real = a * c - b * d
        imag = a * d + b * c

        return str(real) + "+" + str(imag) + "i"
