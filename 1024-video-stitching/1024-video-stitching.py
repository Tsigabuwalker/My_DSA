class Solution:
    def videoStitching(self, clips, time):
        
        # Sort by starting time
        clips.sort()
        
        n = len(clips)
        i = 0
        count = 0
        current_end = 0
        
        while current_end < time:
            
            farthest = current_end
            
            # Extend coverage as far as possible
            while i < n and clips[i][0] <= current_end:
                if clips[i][1] > farthest:
                    farthest = clips[i][1]
                i += 1
            
            # If we can't extend coverage
            if farthest == current_end:
                return -1
            
            count += 1
            current_end = farthest
        
        return count
