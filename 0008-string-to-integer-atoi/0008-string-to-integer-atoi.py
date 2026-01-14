class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # Step 1: Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # Step 2: Handle Signedness
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Conversion
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply sign
        res *= sign
        
        # Step 4: Rounding (Clamping)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res