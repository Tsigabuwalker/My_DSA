class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word = []

        for ch in s:
            if ch == ' ':
                i = len(word) - 1
                while i >= 0:
                    res.append(word[i])
                    i -= 1
                res.append(' ')
                word = []
            else:
                word.append(ch)

        i = len(word) - 1
        while i >= 0:
            res.append(word[i])
            i -= 1

        return "".join(res)
