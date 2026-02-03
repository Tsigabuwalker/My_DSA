import random

class Solution:
    def __init__(self, nums: list[int]):
        self.indices = {}
        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # random.choice gives equal probability to each element in the list
        return random.choice(self.indices[target])