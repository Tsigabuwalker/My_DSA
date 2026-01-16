class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit boundaries
        MAX_INT = 2147483647  # 2^31 - 1
        MIN_INT = -2147483648 # -2^31
        
        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Use absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Main logic: Bit manipulation / Exponential subtraction
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # Double the divisor until it's larger than the remaining dividend
            # temp_divisor << 1 is the same as temp_divisor * 2
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple and update quotient
            dividend -= temp_divisor
            quotient += multiple
            
        return -quotient if negative else quotient