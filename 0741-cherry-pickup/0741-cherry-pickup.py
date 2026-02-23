class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2  # because steps taken are same: r1 + c1 = r2 + c2
            # Check boundaries and thorns
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            # Reached bottom-right
            if r1 == c1 == r2 == c2 == n - 1:
                return grid[r1][c1]
            # Memoization check
            if (r1, c1, c2) in memo:
                return memo[(r1, c1, c2)]

            # Collect cherries
            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            # Explore all 4 move combinations
            next_cherries = max(
                dp(r1 + 1, c1, c2 + 1),  # down, down
                dp(r1, c1 + 1, c2 + 1),  # right, right
                dp(r1 + 1, c1, c2),      # down, right
                dp(r1, c1 + 1, c2)       # right, down
            )

            memo[(r1, c1, c2)] = cherries + next_cherries
            return memo[(r1, c1, c2)]

        return max(0, dp(0, 0, 0))