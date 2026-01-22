class Solution:
    def getPermutation(self, n, k):
        import math

        numbers = list(range(1, n + 1))
        k -= 1  # convert to 0-based
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact

        return "".join(result)
