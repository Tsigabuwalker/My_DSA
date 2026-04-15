class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Pacific (top + left)
        for c in range(n):
            dfs(0, c, pacific)
            dfs(m-1, c, atlantic)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n-1, atlantic)

        # Intersection
        result = list(pacific & atlantic)
        return result