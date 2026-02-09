class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1
        
        # Step 1: Find the range
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        
        # Step 2: Find the actual number
        number_index = (n - 1) // digits
        number = start + number_index
        
        # Step 3: Find the digit in the number
        digit_index = (n - 1) % digits
        return int(str(number)[digit_index])
