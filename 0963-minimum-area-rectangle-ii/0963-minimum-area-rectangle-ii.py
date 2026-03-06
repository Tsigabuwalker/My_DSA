class Solution:
    def minAreaFreeRect(self, points):
        point_set = set()
        for p in points:
            point_set.add((p[0], p[1]))

        n = len(points)
        min_area = float("inf")

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue

                    ax, ay = points[i]
                    bx, by = points[j]
                    cx, cy = points[k]

                    abx = bx - ax
                    aby = by - ay
                    acx = cx - ax
                    acy = cy - ay

                    if abx * acx + aby * acy != 0:
                        continue

                    dx = bx + cx - ax
                    dy = by + cy - ay

                    if (dx, dy) in point_set:
                        side1 = (abx * abx + aby * aby) ** 0.5
                        side2 = (acx * acx + acy * acy) ** 0.5
                        area = side1 * side2

                        if area < min_area:
                            min_area = area

        if min_area == float("inf"):
            return 0
        return min_area