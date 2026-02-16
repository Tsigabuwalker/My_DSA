class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        
        # prev = ways to decode up to i-2
        # curr = ways to decode up to i-1
        prev, curr = 1, 0
        
        # Initialize first character
        if s[0] == '0':
            curr = 0
        elif s[0] == '*':
            curr = 9
        else:
            curr = 1
        
        for i in range(1, n):
            temp = 0
            
            # Single character decoding
            if s[i] == '*':
                temp += 9 * curr
            elif s[i] != '0':
                temp += curr
            # else s[i] == '0' → cannot be decoded alone
            
            # Two characters decoding
            if s[i-1] == '*' and s[i] == '*':
                temp += 15 * prev  # 11-19 and 21-26
            elif s[i-1] == '*':
                if '0' <= s[i] <= '6':
                    temp += 2 * prev  # 1x or 2x
                else:
                    temp += prev      # only 1x
            elif s[i] == '*':
                if s[i-1] == '1':
                    temp += 9 * prev
                elif s[i-1] == '2':
                    temp += 6 * prev
            else:
                two_digit = int(s[i-1:i+1])
                if 10 <= two_digit <= 26:
                    temp += prev
            
            temp %= mod
            prev, curr = curr, temp
        
        return curr
