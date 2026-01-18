class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to jump from the last index, so we go up to n - 1
        for i in range(n - 1):
            # Update the farthest point reachable from current index i
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the range for our current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can already reach the last index, we can stop
                if current_end >= n - 1:
                    break
                    
        return jumps