class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        from functools import lru_cache
        
        n1, n2 = len(s1), len(s2)
        
        @lru_cache(None)
        def dfs(i, j, diff):
            # If both strings are fully consumed
            if i == n1 and j == n2:
                return diff == 0
            
            # Expand numbers in s1
            if i < n1 and s1[i].isdigit():
                val = 0
                for k in range(i, min(i+3, n1)):
                    if s1[k].isdigit():
                        val = val * 10 + int(s1[k])
                        if dfs(k+1, j, diff - val):
                            return True
                    else:
                        break
            
            # Expand numbers in s2
            if j < n2 and s2[j].isdigit():
                val = 0
                for k in range(j, min(j+3, n2)):
                    if s2[k].isdigit():
                        val = val * 10 + int(s2[k])
                        if dfs(i, k+1, diff + val):
                            return True
                    else:
                        break
            
            # Match letters
            if diff == 0:
                if i < n1 and j < n2 and s1[i].isalpha() and s2[j].isalpha() and s1[i] == s2[j]:
                    if dfs(i+1, j+1, diff):
                        return True
            elif diff > 0:
                # s1 has extra letters to consume
                if i < n1 and s1[i].isalpha():
                    if dfs(i+1, j, diff - 1):
                        return True
            else:  # diff < 0
                if j < n2 and s2[j].isalpha():
                    if dfs(i, j+1, diff + 1):
                        return True
            
            return False
        
        return dfs(0, 0, 0)
