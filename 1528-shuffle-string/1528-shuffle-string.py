class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        n = len(s)
        result = [''] * n  # Initialize empty list of length n
        
        for i, char in enumerate(s):
            result[indices[i]] = char  # Place char at its target index
        
        return ''.join(result)
