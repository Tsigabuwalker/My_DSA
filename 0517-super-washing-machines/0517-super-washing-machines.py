class Solution:
    def findMinMoves(self, machines):
        n = len(machines)
        
        total = 0
        for i in range(n):
            total += machines[i]
        
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        prefix_sum = 0
        
        for i in range(n):
            diff = machines[i] - target
            prefix_sum += diff
            
            # take absolute value manually
            if prefix_sum < 0:
                abs_prefix = -prefix_sum
            else:
                abs_prefix = prefix_sum
            
            if diff > max_moves:
                max_moves = diff
            
            if abs_prefix > max_moves:
                max_moves = abs_prefix
        
        return max_moves
