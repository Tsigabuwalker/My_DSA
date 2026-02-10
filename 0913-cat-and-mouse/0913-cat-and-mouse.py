class Solution:
    def catMouseGame(self, graph):
        n = len(graph)

        # dp[m][c][t]: game result
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        # degree[m][c][t]: number of moves available
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                cnt = 0
                for x in graph[c]:
                    if x != 0:
                        cnt += 1
                degree[m][c][1] = cnt

        queue = []

        # Base cases
        for i in range(n):
            for t in range(2):
                if i != 0:
                    dp[0][i][t] = 1
                    queue.append((0, i, t))
                dp[i][i][t] = 2
                queue.append((i, i, t))

        # BFS
        while queue:
            m, c, t = queue.pop(0)
            res = dp[m][c][t]

            if t == 0:
                # parent was cat's turn
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if dp[m][pc][1] != 0:
                        continue
                    if res == 2:
                        dp[m][pc][1] = 2
                        queue.append((m, pc, 1))
                    else:
                        degree[m][pc][1] -= 1
                        if degree[m][pc][1] == 0:
                            dp[m][pc][1] = 1
                            queue.append((m, pc, 1))
            else:
                # parent was mouse's turn
                for pm in graph[m]:
                    if dp[pm][c][0] != 0:
                        continue
                    if res == 1:
                        dp[pm][c][0] = 1
                        queue.append((pm, c, 0))
                    else:
                        degree[pm][c][0] -= 1
                        if degree[pm][c][0] == 0:
                            dp[pm][c][0] = 2
                            queue.append((pm, c, 0))

        return dp[1][2][0]
