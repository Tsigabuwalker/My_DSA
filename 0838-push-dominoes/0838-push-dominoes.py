class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = "L" + dominoes + "R"
        result = []
        i = 0
        
        for j in range(1, len(s)):
            if s[j] == '.':
                continue
            
            middle = j - i - 1
            
            # If same forces
            if s[i] == s[j]:
                result.append(s[i] * middle)
            
            # If L ... R
            elif s[i] == 'L' and s[j] == 'R':
                result.append('.' * middle)
            
            # If R ... L
            else:
                result.append('R' * (middle // 2))
                if middle % 2 == 1:
                    result.append('.')
                result.append('L' * (middle // 2))
            
            if j < len(s) - 1:
                result.append(s[j])
            
            i = j
        
        return ''.join(result)