class Solution:
    def isBoomerang(self, points):
        (x1, y1), (x2, y2), (x3, y3) = points
        
        # Check if slopes are different
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)