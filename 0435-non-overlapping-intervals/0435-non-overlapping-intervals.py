class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time (x[1])
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        # Initialize the end time with the first interval's end
        prev_end = intervals[0][1]
        
        # Start from the second interval
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            if current_start < prev_end:
                # Overlap detected! We greedily remove the one 
                # that ends later (which is the current one)
                removals += 1
            else:
                # No overlap! Update the prev_end to current
                prev_end = current_end
                
        return removals