class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        counts = Counter(s)
        res = []
        
        for char in order:
            if char in counts:
                res.append(char * counts[char])
                del counts[char]
        
        for char, count in counts.items():
            res.append(char * count)
            
        return "".join(res)