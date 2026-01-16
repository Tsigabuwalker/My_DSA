class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found the exact target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the current one is nearer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum