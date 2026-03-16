class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(a: str, b: str, start: int) -> bool:
            # Leading zero check
            if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                return False

            while start < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, start):
                    return False
                start += len(c)
                a, b = b, c
            return True

        # Try all splits for first two numbers
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]
                if valid(a, b, j):
                    return True
        return False
