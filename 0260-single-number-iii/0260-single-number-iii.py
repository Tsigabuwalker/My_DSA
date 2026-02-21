class Solution:
    def singleNumber(self, nums):
        # Step 1: XOR all numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Get rightmost set bit
        diff = xor_all & -xor_all
        
        # Step 3: Divide into two groups
        num1 = 0
        num2 = 0
        
        for num in nums:
            if num & diff:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]