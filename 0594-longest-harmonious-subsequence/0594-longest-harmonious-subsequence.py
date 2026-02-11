from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_length = 0
        
        for x in counts:
            if x + 1 in counts:
                max_length = max(max_length, counts[x] + counts[x + 1])
                
        return max_length