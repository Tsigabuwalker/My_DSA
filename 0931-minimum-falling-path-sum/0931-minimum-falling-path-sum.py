class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        # Start from second row
        for i in range(1, n):
            for j in range(n):
                left = matrix[i-1][j-1] if j-1 >= 0 else float('inf')
                up = matrix[i-1][j]
                right = matrix[i-1][j+1] if j+1 < n else float('inf')
                matrix[i][j] += min(left, up, right)
        
        return min(matrix[-1])