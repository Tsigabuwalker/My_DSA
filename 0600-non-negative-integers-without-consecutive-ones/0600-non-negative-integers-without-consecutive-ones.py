class Solution:
    def findIntegers(self, n: int) -> int:
        # Step 1: precompute Fibonacci numbers
        fib = [0] * 32
        fib[0] = 1  # 0-bit number
        fib[1] = 2  # 1-bit number: 0,1
        for i in range(2, 32):
            fib[i] = fib[i-1] + fib[i-2]
        
        # Step 2: process bits of n
        prev_bit = 0
        result = 0
        # loop from 30th bit to 0
        for i in reversed(range(31)):
            if n & (1 << i):
                result += fib[i]
                if prev_bit == 1:
                    # consecutive ones, stop
                    return result
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1  # include n itself if valid