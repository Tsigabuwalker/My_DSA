from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        
        # Directions: N, E, S, W
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0  # start facing north
        x = y = 0
        max_dist = 0

        for cmd in commands:
            if cmd == -2:          # turn left
                d = (d + 3) % 4
            elif cmd == -1:        # turn right
                d = (d + 1) % 4
            else:                  # move forward
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist
