from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)

        for row in wall:
            pos = 0
            for brick in row[:-1]:  # ignore last edge
                pos += brick
                edge_count[pos] += 1

        max_edges = max(edge_count.values(), default=0)
        return len(wall) - max_edges
