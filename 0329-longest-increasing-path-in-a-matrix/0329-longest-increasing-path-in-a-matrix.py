class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        # Memoization table
        dp = [[0] * n for _ in range(m)]
        
        # Directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            # If already computed
            if dp[r][c] != 0:
                return dp[r][c]
            
            max_length = 1  # At least the cell itself
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    length = 1 + dfs(nr, nc)
                    max_length = max(max_length, length)
            
            dp[r][c] = max_length
            return max_length
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result