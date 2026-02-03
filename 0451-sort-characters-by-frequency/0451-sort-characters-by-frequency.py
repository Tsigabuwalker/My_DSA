
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        counts = Counter(s)
        
        # Step 2: Sort characters by frequency in descending order
        # .most_common() returns a list of (char, count) sorted by count
        sorted_chars = counts.most_common()
        
        # Step 3: Build the resulting string
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
            
        return "".join(result)