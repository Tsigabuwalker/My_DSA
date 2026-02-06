class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), val in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, val))
            graph[b].append((a, 1/val))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0

            visited.add(src)
            for neighbor, weight in graph[src]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, dst, visited)
                if result != -1.0:
                    return result * weight
            return -1.0

        ans = []
        for c, d in queries:
            ans.append(dfs(c, d, set()))
        return ans
