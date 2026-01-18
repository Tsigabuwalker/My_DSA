class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        last_s_ptr = -1
        star_ptr = -1
        
        while s_ptr < len(s):
            # 1. Characters match or pattern has '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # 2. Pattern has '*'
            elif p_ptr < len(p) and p[p_ptr] == '*':
                # Record the position of '*' and the current string position
                star_ptr = p_ptr
                last_s_ptr = s_ptr
                p_ptr += 1
            
            # 3. Mismatch, but we saw a '*' earlier
            elif star_ptr != -1:
                # Backtrack: the last '*' will cover one more character in s
                p_ptr = star_ptr + 1
                last_s_ptr += 1
                s_ptr = last_s_ptr
            
            # 4. Mismatch and no '*' to save us
            else:
                return False
        
        # Check if remaining characters in pattern are all '*'
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)