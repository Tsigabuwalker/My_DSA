class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0
        
        # Iterate from the 31st bit down to the 0th bit
        for i in range(30, -1, -1):
            # The mask helps us extract the prefix of the numbers
            # e.g., if i=30, mask is 100...0. If i=29, mask is 110...0
            mask |= (1 << i)
            
            # Store all prefixes in a set
            prefixes = {num & mask for num in nums}
            
            # Greedy: Try to see if the i-th bit can be 1
            # We "guess" that the next bit of max_xor is 1
            start_max = max_xor | (1 << i)
            
            for p in prefixes:
                # Use the property: if a ^ b = c, then a ^ c = b
                if (p ^ start_max) in prefixes:
                    max_xor = start_max
                    break
                    
        return max_xor