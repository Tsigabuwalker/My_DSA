class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(word, target):
            i = 0
            for char in target:
                if i < len(word) and word[i] == char:
                    i += 1
            return i == len(word)

        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if is_subsequence(word, s):
                return word
                
        return ""