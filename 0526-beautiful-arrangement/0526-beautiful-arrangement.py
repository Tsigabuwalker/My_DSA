from functools import lru_cache

class Solution:
    def countArrangement(self, n: int) -> int:
        
        @lru_cache(None)
        def backtrack(mask):
            # Current position is number of bits set + 1
            pos = bin(mask).count('1') + 1
            
            if pos > n:
                return 1  # all positions filled
            
            total = 0
            for num in range(1, n + 1):
                if not (mask & (1 << (num - 1))):  # num not used
                    if num % pos == 0 or pos % num == 0:
                        total += backtrack(mask | (1 << (num - 1)))
            
            return total
        
        return backtrack(0)
