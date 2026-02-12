class Solution:
    def smallestRange(self, nums):
        k = len(nums)
        
        # Pointers for each list
        pointers = [0] * k
        
        # Initial best range
        best_start = -100000
        best_end = 100000
        
        while True:
            current_min = 100001
            current_max = -100001
            min_index = -1
            
            # Find current min and max
            for i in range(k):
                value = nums[i][pointers[i]]
                
                if value < current_min:
                    current_min = value
                    min_index = i
                
                if value > current_max:
                    current_max = value
            
            # Update best range
            if (current_max - current_min < best_end - best_start) or \
               (current_max - current_min == best_end - best_start and current_min < best_start):
                best_start = current_min
                best_end = current_max
            
            # Move pointer of list that had minimum
            pointers[min_index] += 1
            
            # If any list is exhausted → stop
            if pointers[min_index] == len(nums[min_index]):
                break
        
        return [best_start, best_end]
