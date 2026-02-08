class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        max_count = 0
        max_char = 0
        for i in range(26):
            if count[i] > max_count:
                max_count = count[i]
                max_char = i

        if max_count > (n + 1) // 2:
            return ""

        result = [""] * n
        idx = 0

        while count[max_char] > 0:
            result[idx] = chr(max_char + ord('a'))
            idx += 2
            count[max_char] -= 1

        for i in range(26):
            while count[i] > 0:
                if idx >= n:
                    idx = 1
                result[idx] = chr(i + ord('a'))
                idx += 2
                count[i] -= 1

        return "".join(result)
