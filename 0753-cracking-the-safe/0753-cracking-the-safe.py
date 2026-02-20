class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        ans = []

        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        start = "0" * (n - 1)
        dfs(start)
        return "".join(ans) + start