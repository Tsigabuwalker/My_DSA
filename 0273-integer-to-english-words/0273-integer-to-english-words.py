class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                 "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def threeDigitsToWords(n):
            res = []
            if n >= 100:
                res.append(ones[n // 100] + " Hundred")
                n %= 100
            if 10 <= n <= 19:
                res.append(teens[n - 10])
            else:
                if n >= 20:
                    res.append(tens[n // 10])
                    n %= 10
                if n > 0:
                    res.append(ones[n])
            return " ".join(res)

        res = []
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                res.append(threeDigitsToWords(num % 1000) + (" " + unit if unit else ""))
            num //= 1000
            if num == 0:
                break

        return " ".join(res[::-1])
