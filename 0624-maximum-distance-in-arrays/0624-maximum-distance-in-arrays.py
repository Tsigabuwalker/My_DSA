class Solution:
    def maxDistance(self, arrays):
        # Initialize using first array
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        
        max_dist = 0
        
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate possible distances
            dist1 = current_max - global_min
            if dist1 < 0:
                dist1 = -dist1
            
            dist2 = global_max - current_min
            if dist2 < 0:
                dist2 = -dist2
            
            # Update maximum distance
            if dist1 > max_dist:
                max_dist = dist1
            if dist2 > max_dist:
                max_dist = dist2
            
            # Update global min and max
            if current_min < global_min:
                global_min = current_min
            
            if current_max > global_max:
                global_max = current_max
        
        return max_dist
