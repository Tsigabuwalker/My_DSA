class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        if n == 1:
            return ""
        
        chars = list(palindrome)
        
        # Check first half only
        for i in range(n // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return "".join(chars)
        
        # If all first half are 'a'
        chars[-1] = 'b'
        return "".join(chars)
