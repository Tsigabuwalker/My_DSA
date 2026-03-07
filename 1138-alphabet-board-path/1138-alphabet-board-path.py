class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Board layout (row, col) for each letter
        pos = {}
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                pos[board[r][c]] = (r, c)
        
        # Start at 'a' = (0,0)
        cr, cc = 0, 0
        result = []
        
        for char in target:
            tr, tc = pos[char]  # target row, col
            
            # Special handling for 'z' — we must move horizontally first when going TO 'z'
            # and vertically first when leaving 'z' (to avoid going off-board)
            if char == 'z':
                # When moving TO z: horizontal first, then down
                if tc > cc:
                    result.append('R' * (tc - cc))
                elif tc < cc:
                    result.append('L' * (cc - tc))
                # Then vertical
                if tr > cr:
                    result.append('D' * (tr - cr))
                elif tr < cr:
                    result.append('U' * (cr - tr))
            else:
                # Normal case: prefer vertical first, then horizontal
                # (this works for all letters except when target is 'z')
                if tr > cr:
                    result.append('D' * (tr - cr))
                elif tr < cr:
                    result.append('U' * (cr - tr))
                
                if tc > cc:
                    result.append('R' * (tc - cc))
                elif tc < cc:
                    result.append('L' * (cc - tc))
            
            # Add the character
            result.append('!')
            
            # Update current position
            cr, cc = tr, tc
        
        return ''.join(result)