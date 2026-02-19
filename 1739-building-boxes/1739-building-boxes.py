class Solution:
    def minimumBoxes(self, n: int) -> int:
        total = 0
        k = 0
        
        # Build full pyramid layers
        while total + (k + 1) * (k + 2) // 2 <= n:
            k += 1
            total += k * (k + 1) // 2
        
        # Now add extra boxes to floor one by one
        floor = k * (k + 1) // 2
        remaining = n - total
        
        extra = 0
        while remaining > 0:
            extra += 1
            remaining -= extra
        
        return floor + extra
