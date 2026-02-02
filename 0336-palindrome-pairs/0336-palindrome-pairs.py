from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        word_to_index = {word: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: If prefix is palindrome, look for reversed suffix
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in word_to_index and word_to_index[back] != i:
                        res.append([word_to_index[back], i])

                # Case 2: If suffix is palindrome, look for reversed prefix
                # j != n to avoid duplicates
                if j != n and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back in word_to_index and word_to_index[back] != i:
                        res.append([i, word_to_index[back]])

        return res
