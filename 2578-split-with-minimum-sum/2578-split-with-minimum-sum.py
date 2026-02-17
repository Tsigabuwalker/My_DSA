class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        
        num1 = []
        num2 = []
        
        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1.append(d)
            else:
                num2.append(d)
        
        return int("".join(num1)) + int("".join(num2))
