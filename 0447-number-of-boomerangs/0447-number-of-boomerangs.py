class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        total_boomerangs = 0
        
        for p1 in points:
            # Hash map to store frequency of distances from current pivot p1
            distance_map = {}
            
            for p2 in points:
                # Calculate squared distance
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                d2 = dx*dx + dy*dy
                
                # Increment the count for this distance
                distance_map[d2] = distance_map.get(d2, 0) + 1
            
            # For each distance group, calculate permutations
            for dist in distance_map:
                m = distance_map[dist]
                # If m points have the same distance, we can pick any 2: m * (m - 1)
                total_boomerangs += m * (m - 1)
                
        return total_boomerangs