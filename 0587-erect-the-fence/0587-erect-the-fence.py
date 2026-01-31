class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        if len(trees) <= 1:
            return trees

        # Cross product
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Sort points
        trees.sort()

        lower = []
        for p in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(tuple(p))

        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(tuple(p))

        # Remove duplicate endpoints
        hull = set(lower[:-1] + upper[:-1])
        return list(hull)
