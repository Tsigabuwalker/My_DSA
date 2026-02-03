from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
            
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1])
        
        if s1_counts == window_counts:
            return True
            
        for i in range(n1, n2):
            new_char = s2[i]
            old_char = s2[i - n1]
            
            window_counts[new_char] += 1
            window_counts[old_char] -= 1
            
            if window_counts[old_char] == 0:
                del window_counts[old_char]
                
            if s1_counts == window_counts:
                return True
                
        return False