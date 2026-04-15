class Solution:
    def findDiagonalOrder(self, mat):
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        
        r = c = 0
        direction = 1  # 1 = up-right, -1 = down-left

        for _ in range(m * n):
            result.append(mat[r][c])

            if direction == 1:  # up-right
                if c == n - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:  # down-left
                if r == m - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return result