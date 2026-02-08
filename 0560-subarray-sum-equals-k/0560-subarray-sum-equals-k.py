class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            diff = current_sum - k
            
            if diff in prefix_sums:
                count += prefix_sums[diff]
            
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count