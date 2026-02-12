class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        parent = [i for i in range(n * n * 4)]  # 4 triangles per cell

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)  # base index for cell (i,j)
                val = grid[i][j]
                
                # Inside the cell
                if val == '/':
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif val == '\\':
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:  # ' '
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)

                # Connect with cell below
                if i + 1 < n:
                    union(index + 2, 4 * ((i + 1) * n + j) + 0)
                # Connect with cell to the right
                if j + 1 < n:
                    union(index + 1, 4 * (i * n + j + 1) + 3)

        # Count number of unique components
        regions = sum(parent[i] == i for i in range(n * n * 4))
        return regions
