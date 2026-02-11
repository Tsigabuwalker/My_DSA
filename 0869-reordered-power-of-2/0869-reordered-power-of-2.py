class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Helper function to count digits
        def count_digits(x):
            return sorted(str(x))
        
        target = count_digits(n)
        
        # Check all powers of 2 up to 2^30
        for i in range(31):
            if count_digits(1 << i) == target:
                return True
        
        return False
