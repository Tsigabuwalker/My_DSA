from collections import Counter

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)
        pair_count = 0
        
        for x in counts:
            if k > 0:
                if x + k in counts:
                    pair_count += 1
            else:
                if counts[x] > 1:
                    pair_count += 1
                    
        return pair_count