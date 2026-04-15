class Solution:
    def countBattleships(self, board):
        if not board:
            return 0

        m, n = len(board), len(board[0])
        count = 0

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    # check top
                    if r > 0 and board[r-1][c] == 'X':
                        continue
                    # check left
                    if c > 0 and board[r][c-1] == 'X':
                        continue
                    
                    count += 1

        return count