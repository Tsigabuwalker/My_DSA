class Solution:
    def movesToChessboard(self, board):
        n = len(board)

        # Convert rows to integers for easier comparison
        rows = [tuple(row) for row in board]
        first_row = rows[0]
        complement_row = tuple(1 - x for x in first_row)

        # Check validity of rows
        for row in rows:
            if row != first_row and row != complement_row:
                return -1

        # Check validity of columns
        cols = [tuple(board[i][j] for i in range(n)) for j in range(n)]
        first_col = cols[0]
        complement_col = tuple(1 - x for x in first_col)

        for col in cols:
            if col != first_col and col != complement_col:
                return -1

        # Count number of 1s in first row and column
        row_sum = sum(first_row)
        col_sum = sum(first_col)

        # Check counts are valid
        if not (n//2 <= row_sum <= (n+1)//2) or not (n//2 <= col_sum <= (n+1)//2):
            return -1

        # Count mismatches
        row_swaps = sum(first_row[i] == i % 2 for i in range(n))
        col_swaps = sum(first_col[i] == i % 2 for i in range(n))

        if n % 2 == 0:
            row_swaps = min(row_swaps, n - row_swaps)
            col_swaps = min(col_swaps, n - col_swaps)
        else:
            if row_swaps % 2 == 1:
                row_swaps = n - row_swaps
            if col_swaps % 2 == 1:
                col_swaps = n - col_swaps

        return (row_swaps + col_swaps) // 2
