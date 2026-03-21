class Solution:
    def numIdenticalPairs(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        res = 0
        
        for v in count.values():
            res += v * (v - 1) // 2
        
        return res