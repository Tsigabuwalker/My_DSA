class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # min possible open '('
        high = 0  # max possible open '('

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # treat '*' as ')'
                high += 1  # treat '*' as '('
            
            # Cannot have negative min open
            low = max(low, 0)

            # Too many ')' → impossible
            if high < 0:
                return False

        return low == 0
