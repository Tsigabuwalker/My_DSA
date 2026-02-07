class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        n = len(s)
        i = 0

        while i < n:
            end = i + k
            if end > n:
                end = n

            j = end - 1
            while j >= i:
                res.append(s[j])
                j -= 1

            j = end
            while j < i + 2 * k and j < n:
                res.append(s[j])
                j += 1

            i += 2 * k

        return "".join(res)
