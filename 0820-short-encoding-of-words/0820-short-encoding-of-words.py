class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        unique = {}
        for w in words:
            unique[w] = True
        
        for w in words:
            for k in range(1, len(w)):
                suffix = w[k:]
                if suffix in unique:
                    del unique[suffix]
        
        total = 0
        for w in unique:
            total += len(w) + 1
        return total
