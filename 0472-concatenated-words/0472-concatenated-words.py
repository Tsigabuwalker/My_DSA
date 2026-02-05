class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = {w for w in words if w}
        memo = {}

        def can_form(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in word_set:
                    if suffix in word_set or can_form(suffix):
                        memo[word] = True
                        return True
            
            memo[word] = False
            return False

        res = []
        for w in words:
            if can_form(w):
                res.append(w)
        return res
