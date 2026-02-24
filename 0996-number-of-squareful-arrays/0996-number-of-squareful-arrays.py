from collections import Counter
import math

class Solution:
    def numSquarefulPerms(self, nums):
        n = len(nums)
        nums_count = Counter(nums)
        nums_unique = list(nums_count.keys())

        # Build adjacency: two numbers can be adjacent if sum is a perfect square
        graph = {x: [] for x in nums_unique}
        for i, x in enumerate(nums_unique):
            for j, y in enumerate(nums_unique):
                if i == j and nums_count[x] == 1:
                    continue
                if math.isqrt(x + y) ** 2 == x + y:
                    graph[x].append(y)

        res = 0

        def backtrack(path, count):
            nonlocal res
            if len(path) == n:
                res += 1
                return
            last = path[-1] if path else None
            for next_num in (graph[last] if last is not None else nums_unique):
                if count[next_num] > 0:
                    count[next_num] -= 1
                    path.append(next_num)
                    backtrack(path, count)
                    path.pop()
                    count[next_num] += 1

        backtrack([], nums_count.copy())
        return res