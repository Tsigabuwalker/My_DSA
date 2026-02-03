class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        
        # Helper function to get the next index
        def get_next(curr_idx):
            # (current index + jump) % length handles circularity
            return (curr_idx + nums[curr_idx]) % n
        
        for i in range(n):
            if nums[i] == 0: # Already visited and marked as non-cycle
                continue
            
            slow = i
            fast = get_next(i)
            
            # Ensure the fast pointer and its next step are moving in the same direction as the start
            while nums[fast] * nums[i] > 0 and nums[get_next(fast)] * nums[i] > 0:
                if slow == fast:
                    # Check for self-loop (cycle of length 1)
                    if slow == get_next(slow):
                        break
                    return True
                
                slow = get_next(slow)
                fast = get_next(get_next(fast))
            
            # Optimization: Mark all nodes in this failed path as 0
            # If we couldn't find a cycle starting here, these nodes won't lead to one later
            curr = i
            val = nums[i]
            while nums[curr] * val > 0:
                next_node = get_next(curr)
                nums[curr] = 0
                curr = next_node
                
        return False