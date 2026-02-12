class Solution:
    def smallestRange(self, nums):
        k = len(nums)
        flat = []
        
        # Step 1: Flatten the list with (value, list_index)
        for i in range(k):
            for val in nums[i]:
                flat.append((val, i))
        
        # Step 2: Sort the flat list by value
        flat.sort(key=lambda x: x[0])
        
        # Step 3: Sliding window
        count = [0] * k
        inside = 0
        left = 0
        best_start, best_end = -100000, 100000
        
        for right in range(len(flat)):
            val, idx = flat[right]
            if count[idx] == 0:
                inside += 1
            count[idx] += 1
            
            # Try shrinking window
            while inside == k:
                start_val, start_idx = flat[left]
                
                # Update best range
                if val - start_val < best_end - best_start or \
                   (val - start_val == best_end - best_start and start_val < best_start):
                    best_start, best_end = start_val, val
                
                # Move left pointer
                count[start_idx] -= 1
                if count[start_idx] == 0:
                    inside -= 1
                left += 1
        
        return [best_start, best_end]
