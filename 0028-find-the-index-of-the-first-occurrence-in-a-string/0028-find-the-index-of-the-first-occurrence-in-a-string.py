class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # If the needle is longer than the haystack, it can't be found
        for i in range(n - m + 1):
            # Check if the substring starting at i matches needle
            if haystack[i : i + m] == needle:
                return i
                
        return -1