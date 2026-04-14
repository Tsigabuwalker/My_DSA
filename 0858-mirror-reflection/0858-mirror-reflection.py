class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Reduce p and q by removing common factors of 2
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
        
        # Decide based on parity
        if p % 2 == 1 and q % 2 == 1:
            return 1
        elif p % 2 == 1 and q % 2 == 0:
            return 0
        else:
            return 2