class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target

        step = 0
        total = 0

        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step

        return step
