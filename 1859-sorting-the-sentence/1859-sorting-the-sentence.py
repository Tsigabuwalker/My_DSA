class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # Split by space
        n = len(words)
        res = [""] * n
        
        for word in words:
            # Last character is the position
            pos = int(word[-1]) - 1  # Convert to 0-index
            res[pos] = word[:-1]     # Remove the number
        
        return " ".join(res)
