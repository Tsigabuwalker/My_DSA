import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.available_count = self.total
        self.mapping = {}

    def flip(self) -> list[int]:
        r = random.randint(0, self.available_count - 1)
        self.available_count -= 1
        
        actual_idx = self.mapping.get(r, r)
        last_val = self.mapping.get(self.available_count, self.available_count)
        
        self.mapping[r] = last_val
        
        return [actual_idx // self.n, actual_idx % self.n]

    def reset(self) -> None:
        self.mapping.clear()
        self.available_count = self.total