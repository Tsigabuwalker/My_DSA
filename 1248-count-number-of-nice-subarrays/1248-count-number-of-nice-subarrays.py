class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def at_most_k_odd(k: int) -> int:
            left = 0
            odd_count = 0
            result = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k and left <= right:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                result += right - left + 1
            
            return result
        
        # Number of subarrays with exactly k odds
        # = number with at most k odds − number with at most (k-1) odds
        return at_most_k_odd(k) - at_most_k_odd(k - 1)