class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # assign the maximum possible value to cell (i,j)
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
        
        return matrix
