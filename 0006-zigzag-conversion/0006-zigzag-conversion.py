class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only one row or string is too short, return as is
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings for each row
        rows = ["" for _ in range(numRows)]
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # Flip direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move row pointer
            current_row += 1 if going_down else -1
            
        return "".join(rows)