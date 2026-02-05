class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x[1] < pivot[1]]
            middle = [x for x in arr if x[1] == pivot[1]]
            right = [x for x in arr if x[1] > pivot[1]]
            return quicksort(left) + middle + quicksort(right)

        sorted_points = quicksort(points)
        
        arrows = 1
        current_end = sorted_points[0][1]
        
        for i in range(1, len(sorted_points)):
            if sorted_points[i][0] > current_end:
                arrows += 1
                current_end = sorted_points[i][1]
                
        return arrows