from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def isMagic(r, c):
            nums = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    nums.add(grid[i][j])

            if len(nums) != 9 or grid[r + 1][c + 1] != 5:
                return False

            s = 15
            return (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] == s and
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == s and
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == s and
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == s and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == s and
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == s and
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == s
            )

        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count
