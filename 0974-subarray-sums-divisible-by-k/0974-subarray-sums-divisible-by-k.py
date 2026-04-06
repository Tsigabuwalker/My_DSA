class Solution:
    def subarraysDivByK(self, nums, k):
        count = {0: 1}  # remainder 0 seen once
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            
            remainder = prefix_sum % k
            
            # Handle negative remainder
            if remainder < 0:
                remainder += k
            
            if remainder in count:
                result += count[remainder]
            
            count[remainder] = count.get(remainder, 0) + 1
        
        return result