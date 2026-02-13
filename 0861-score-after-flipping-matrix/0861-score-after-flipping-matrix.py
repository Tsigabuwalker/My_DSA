class Solution:
    def matrixScore(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # Step 1: Make sure the first column is all 1's
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1  # toggle the row
        
        # Step 2: Maximize 1's in each column
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            if ones < m - ones:  # more 0's than 1's
                for i in range(m):
                    grid[i][j] ^= 1  # toggle the column
        
        # Step 3: Compute the total score
        total = 0
        for i in range(m):
            num = 0
            for j in range(n):
                num = (num << 1) | grid[i][j]
            total += num
        
        return total
