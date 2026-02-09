class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total = 0
        n = len(nums)
        
        for i in range(32):
            count_ones = 0
            for num in nums:
                count_ones += (num >> i) & 1
            
            total += count_ones * (n - count_ones)
            
        return total