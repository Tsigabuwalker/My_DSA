class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        d = distance
        n = len(d)

        for i in range(3, n):
            # Case 1
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True

            # Case 2
            if i >= 4 and d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True

            # Case 3
            if (
                i >= 5 and
                d[i-2] >= d[i-4] and
                d[i] >= d[i-2] - d[i-4] and
                d[i-1] >= d[i-3] - d[i-5] and
                d[i-1] <= d[i-3]
            ):
                return True

        return False
