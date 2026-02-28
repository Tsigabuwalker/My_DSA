class Solution:
    def kClosest(self, points, k):
        self.quickSelect(points, 0, len(points) - 1, k)
        return points[:k]

    def quickSelect(self, points, left, right, k):
        if left >= right:
            return
        
        pivot_index = self.partition(points, left, right)
        
        if pivot_index == k:
            return
        elif pivot_index < k:
            self.quickSelect(points, pivot_index + 1, right, k)
        else:
            self.quickSelect(points, left, pivot_index - 1, k)

    def partition(self, points, left, right):
        pivot = self.distance(points[right])
        i = left
        
        for j in range(left, right):
            if self.distance(points[j]) <= pivot:
                points[i], points[j] = points[j], points[i]
                i += 1
        
        points[i], points[right] = points[right], points[i]
        return i

    def distance(self, point):
        return point[0] * point[0] + point[1] * point[1]