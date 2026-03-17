import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # Pick a random number in [1, total]
        target = random.randint(1, self.total)
        # Binary search to find index
        return bisect.bisect_left(self.prefix, target)


# Example usage:
sol = Solution([1])
print(sol.pickIndex())  # Always 0

sol = Solution([1,3])
results = [sol.pickIndex() for _ in range(10)]
print(results)  # More 1s than 0s, roughly 75% vs 25%
