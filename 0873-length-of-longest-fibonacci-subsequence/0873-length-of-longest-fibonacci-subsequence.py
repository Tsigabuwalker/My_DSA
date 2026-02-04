class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        pos = {}
        for i in range(n):
            pos[arr[i]] = i

        dp = [[2] * n for _ in range(n)]
        res = 0

        for j in range(n):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev in pos:
                    k = pos[prev]
                    if k < i:
                        dp[i][j] = dp[k][i] + 1
                        if dp[i][j] > res:
                            res = dp[i][j]

        return res
