class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Top and bottom
                    area += 2
                    
                    # 4 sides
                    # Up
                    area += max(grid[i][j] - (grid[i-1][j] if i > 0 else 0), 0)
                    # Down
                    area += max(grid[i][j] - (grid[i+1][j] if i < n-1 else 0), 0)
                    # Left
                    area += max(grid[i][j] - (grid[i][j-1] if j > 0 else 0), 0)
                    # Right
                    area += max(grid[i][j] - (grid[i][j+1] if j < n-1 else 0), 0)
        
        return area
