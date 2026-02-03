class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = {}
        for c in "qwertyuiop": rows[c] = 0
        for c in "asdfghjkl": rows[c] = 1
        for c in "zxcvbnm": rows[c] = 2
        
        res = []
        for word in words:
            lower_word = word.lower()
            row_idx = rows[lower_word[0]]
            
            is_valid = True
            for char in lower_word:
                if rows[char] != row_idx:
                    is_valid = False
                    break
            
            if is_valid:
                res.append(word)
                
        return res
