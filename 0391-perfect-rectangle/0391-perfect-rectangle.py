class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        area = 0
        corners = set()
        
        # Initialize boundaries with infinity
        min_x, min_y = float('inf'), float('inf')
        max_a, max_b = float('-inf'), float('-inf')
        
        for x, y, a, b in rectangles:
            # Update the large bounding box coordinates
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            
            # Add up the area
            area += (a - x) * (b - y)
            
            # Record corners and use XOR-like logic with the set
            # If a corner exists, remove it; if not, add it.
            for point in [(x, y), (x, b), (a, y), (a, b)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)
        
        # Check Condition 1: Total Area
        expected_area = (max_a - min_x) * (max_b - min_y)
        if area != expected_area:
            return False
            
        # Check Condition 2: The four corners of the bounding box
        # must be the only ones left in the set
        expected_corners = {(min_x, min_y), (min_x, max_b), (max_a, min_y), (max_a, max_b)}
        
        return corners == expected_corners