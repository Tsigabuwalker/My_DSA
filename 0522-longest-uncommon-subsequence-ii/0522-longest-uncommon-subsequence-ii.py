class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def is_subsequence(s1, s2):
            i = 0
            for char in s2:
                if i < len(s1) and s1[i] == char:
                    i += 1
            return i == len(s1)

        strs.sort(key=len, reverse=True)
        
        for i, s1 in enumerate(strs):
            is_uncommon = True
            for j, s2 in enumerate(strs):
                if i == j:
                    continue
                if is_subsequence(s1, s2):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                return len(s1)
                
        return -1