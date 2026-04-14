import math

class Solution:
    def isGoodArray(self, nums):
        g = nums[0]
        
        for num in nums[1:]:
            g = math.gcd(g, num)
            if g == 1:
                return True  # early stop
        
        return g == 1