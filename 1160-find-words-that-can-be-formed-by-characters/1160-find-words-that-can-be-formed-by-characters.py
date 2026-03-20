class Solution:
    def countCharacters(self, words, chars):
        from collections import Counter
        
        char_count = Counter(chars)
        total = 0
        
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= char_count[c] for c in word):
                total += len(word)
        
        return total