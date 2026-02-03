from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:p_len])
        
        result = []
        
        # Check the first window
        if s_count == p_count:
            result.append(0)
            
        # Slide the window across the rest of s
        for i in range(1, s_len - p_len + 1):
            # The character entering the window is s[i + p_len - 1]
            new_char = s[i + p_len - 1]
            # The character leaving the window is s[i - 1]
            old_char = s[i - 1]
            
            s_count[new_char] += 1
            s_count[old_char] -= 1
            
            # Clean up the counter to keep comparison efficient
            if s_count[old_char] == 0:
                del s_count[old_char]
                
            if s_count == p_count:
                result.append(i)
                
        return result