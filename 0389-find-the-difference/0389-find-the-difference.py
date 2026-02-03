class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        # XOR all characters in string s
        for char in s:
            res ^= ord(char)
            
        # XOR all characters in string t
        for char in t:
            res ^= ord(char)
            
        # The result is the ASCII value of the added character
        return chr(res)