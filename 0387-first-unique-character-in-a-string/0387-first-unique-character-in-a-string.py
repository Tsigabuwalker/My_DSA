class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count the frequency of each character
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        # Step 2: Find the first character with a count of 1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
                
        return -1