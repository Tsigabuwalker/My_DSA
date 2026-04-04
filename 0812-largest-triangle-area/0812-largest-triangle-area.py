class Solution:
    def largestTriangleArea(self, points):
        """
        :param points: List[List[int]]
        :return: float
        """
        n = len(points)
        max_area = 0.0

        # Try all combinations of 3 points
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    
                    # Shoelace formula
                    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0
                    max_area = max(max_area, area)

        return max_area


# Example usage
sol = Solution()
print(sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))  # Output: 2.0
print(sol.largestTriangleArea([[1,0],[0,0],[0,1]]))              # Output: 0.5
