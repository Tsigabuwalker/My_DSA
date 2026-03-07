class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        n = len(hours)
        
        # Convert hours to +1 (tiring) or -1 (non-tiring)
        score = [1 if h > 8 else -1 for h in hours]
        
        # prefix[0] = 0, prefix[i+1] = sum of first i+1 days
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + score[i]
        
        # Keep track of the FIRST (leftmost) occurrence of each prefix sum
        first_occurrence = {}
        max_length = 0
        
        for j in range(n + 1):
            curr = prefix[j]
            
            # Case 1: prefix from index 0 to j is already positive
            if curr > 0:
                max_length = max(max_length, j)
            
            # Case 2: look for the leftmost position where prefix[i] == curr - 1
            # because curr - (curr-1) = 1 > 0
            target = curr - 1
            if target in first_occurrence:
                i = first_occurrence[target]
                max_length = max(max_length, j - i)
            
            # Record the earliest occurrence of this prefix value
            if curr not in first_occurrence:
                first_occurrence[curr] = j
        
        return max_length