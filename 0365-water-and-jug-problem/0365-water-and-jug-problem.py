import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Condition 1: The target cannot be more than the combined capacity
        if target > x + y:
            return False
        
        # Condition 2: The target must be a multiple of the GCD of x and y
        # This is based on Bézout's Identity
        return target % math.gcd(x, y) == 0