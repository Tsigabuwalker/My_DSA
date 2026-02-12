class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        
        # Directions for 8 neighbors
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),         (0,1),
                      (1,-1), (1,0),  (1,1)]
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] == 1 or board[ni][nj] == 2:  # 2 = was live
                            live_neighbors += 1
                
                # Rule 1 or 3: live cell dies
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2  # mark as live -> dead
                
                # Rule 4: dead cell becomes live
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 3  # mark as dead -> live
        
        # Update the board to final state
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
