class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in map(str, range(1, 10)):
                        if self.is_valid(board, r, c, num):
                            board[r][c] = num
                            
                            if self.solve(board):
                                return True
                            
                            # Backtrack
                            board[r][c] = '.'
                    return False
        return True

    def is_valid(self, board, row, col, num):
        for i in range(9):
            # Check row
            if board[row][i] == num:
                return False
            # Check column
            if board[i][col] == num:
                return False
            # Check 3x3 sub-box
            # (row // 3 * 3) finds the starting row index of the box
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True