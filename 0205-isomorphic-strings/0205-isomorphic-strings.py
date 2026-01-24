class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}
        mapped_chars = set()
        
        for c1, c2 in zip(s, t):
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            else:
                if c2 in mapped_chars:
                    return False
                mapping[c1] = c2
                mapped_chars.add(c2)
        
        return True
