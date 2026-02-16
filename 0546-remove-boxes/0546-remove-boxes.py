from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes):
        
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            
            # Merge same colors at the end
            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            
            # Option 1: remove last group immediately
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            
            # Option 2: try merging with same color earlier
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res,
                              dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            
            return res
        
        return dp(0, len(boxes) - 1, 0)
