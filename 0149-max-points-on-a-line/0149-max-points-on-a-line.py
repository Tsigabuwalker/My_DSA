from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    slope = (1, 0)      # vertical
                elif dy == 0:
                    slope = (0, 1)      # horizontal
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    # normalize direction
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] += 1

            ans = max(ans, max(slopes.values(), default=0) + 1)

        return ans
