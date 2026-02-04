class Solution:
    def removeStones(self, stones):
        from collections import defaultdict

        # Build adjacency list: stones share row or column
        graph = defaultdict(list)
        n = len(stones)
        for i in range(n):
            x1, y1 = stones[i]
            for j in range(i + 1, n):
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)

        # Count connected components
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return n - components
