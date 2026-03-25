from collections import defaultdict

class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Step 1: Collect elements
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        
        # Step 2: Sort each diagonal
        for key in diagonals:
            diagonals[key].sort(reverse=True)  # reverse for efficient pop()
        
        # Step 3: Place back
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        
        return mat