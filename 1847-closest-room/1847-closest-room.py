class Solution:
    def closestRoom(self, rooms, queries):
        import bisect
        
        # Sort rooms by size descending
        rooms.sort(key=lambda x: -x[1])
        
        # Add index to queries and sort by minSize descending
        indexed_queries = [(p, m, i) for i, (p, m) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: -x[1])
        
        result = [-1] * len(queries)
        valid_ids = []
        
        i = 0  # pointer for rooms
        
        for preferred, minSize, idx in indexed_queries:
            
            # Add all rooms that satisfy size condition
            while i < len(rooms) and rooms[i][1] >= minSize:
                bisect.insort(valid_ids, rooms[i][0])
                i += 1
            
            if not valid_ids:
                result[idx] = -1
                continue
            
            # Binary search closest to preferred
            pos = bisect.bisect_left(valid_ids, preferred)
            
            best = float('inf')
            
            # Check right neighbor
            if pos < len(valid_ids):
                best = valid_ids[pos]
            
            # Check left neighbor
            if pos > 0:
                left_id = valid_ids[pos - 1]
                
                if best == float('inf') or \
                   abs(left_id - preferred) <= abs(best - preferred):
                    best = left_id
            
            result[idx] = best
        
        return result
