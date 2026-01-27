class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        # lps[i] stores the length of the longest happy prefix for s[0...i]
        lps = [0] * n
        j = 0  
        
        for i in range(1, n):
            # If there is a mismatch, move j back using the lps table
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
                
            # If characters match, increment the prefix length
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                
        # Return the prefix of length lps[-1]
        return s[:lps[-1]]