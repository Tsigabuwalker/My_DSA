class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones_count = 0
        flips = 0
        
        for ch in s:
            if ch == '1':
                ones_count += 1
            else:  # ch == '0'
                flips = min(flips + 1, ones_count)
        
        return flips