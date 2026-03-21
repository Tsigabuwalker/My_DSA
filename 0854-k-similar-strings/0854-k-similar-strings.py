from collections import deque

class Solution:
    def kSimilarity(self, s1, s2):
        if s1 == s2:
            return 0
        
        queue = deque([(s1, 0)])
        visited = set([s1])
        
        while queue:
            curr, step = queue.popleft()
            
            if curr == s2:
                return step
            
            i = 0
            while curr[i] == s2[i]:
                i += 1
            
            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    new = list(curr)
                    new[i], new[j] = new[j], new[i]
                    new = ''.join(new)
                    
                    if new not in visited:
                        visited.add(new)
                        queue.append((new, step + 1))