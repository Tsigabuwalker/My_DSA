class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        open_count = 0   # unmatched '('
        moves = 0        # insertions needed
        
        for ch in s:
            
            if ch == '(':
                open_count += 1
            
            else:  # ch == ')'
                if open_count > 0:
                    open_count -= 1   # match with previous '('
                else:
                    moves += 1        # need to insert '('
        
        # remaining '(' need ')'
        moves += open_count
        
        return moves
