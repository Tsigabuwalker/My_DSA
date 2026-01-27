class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)
        
        # 1. Precompute KMP LPS array for 'evil'
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = lps[j-1]
            if evil[i] == evil[j]:
                j += 1
            lps[i] = j
            
        # Function to determine next evil_match_len given current len and next char
        def get_next_match(curr_match, char):
            while curr_match > 0 and char != evil[curr_match]:
                curr_match = lps[curr_match - 1]
            if char == evil[curr_match]:
                curr_match += 1
            return curr_match

        memo = {}

        def dp(idx, e_idx, is_less, is_greater):
            # If we matched the whole 'evil' string, this path is dead
            if e_idx == m: return 0
            # If we reached the end of the string length n, we found 1 good string
            if idx == n: return 1
            
            state = (idx, e_idx, is_less, is_greater)
            if state in memo: return memo[state]
            
            res = 0
            # Define the range of characters we can use at this position
            lower = s1[idx] if not is_greater else 'a'
            upper = s2[idx] if not is_less else 'z'
            
            for char_code in range(ord(lower), ord(upper) + 1):
                c = chr(char_code)
                
                new_is_greater = is_greater or (c > lower)
                new_is_less = is_less or (c < upper)
                new_e_idx = get_next_match(e_idx, c)
                
                res = (res + dp(idx + 1, new_e_idx, new_is_less, new_is_greater)) % MOD
                
            memo[state] = res
            return res

        return dp(0, 0, False, False)