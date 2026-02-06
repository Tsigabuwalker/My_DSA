class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        
        # Case 1: all uppercase
        if word.upper() == word:
            return True
        
        # Case 2: all lowercase
        if word.lower() == word:
            return True
        
        # Case 3: first letter uppercase, rest lowercase
        if word[0].isupper() and word[1:].lower() == word[1:]:
            return True
        
        return False

