class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Starting position
        x, y = 0, 0
        
        # Store visited coordinates as tuples (tuples are hashable)
        visited = {(0, 0)}
        
        # Direction mapping
        moves = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        
        for direction in path:
            # Update current position
            dx, dy = moves[direction]
            x += dx
            y += dy
            
            # If current position was already visited, the path crossed itself
            if (x, y) in visited:
                return True
            
            # Otherwise, add to the set
            visited.add((x, y))
            
        return False