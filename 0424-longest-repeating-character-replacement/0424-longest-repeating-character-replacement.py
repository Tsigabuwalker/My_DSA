class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            # Update frequency of the current character
            count[s[r]] = count.get(s[r], 0) + 1
            # Update the max frequency found in the window so far
            max_freq = max(max_freq, count[s[r]])
            
            # Current window length is (r - l + 1)
            # If characters to replace > k, shrink the window
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            # Update the result
            max_length = max(max_length, r - l + 1)
            
        return max_length