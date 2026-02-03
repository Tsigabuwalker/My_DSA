class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Count characters in the magazine
        # We can use an array of size 26 or a hash map
        counts = {}
        for char in magazine:
            counts[char] = counts.get(char, 0) + 1
            
        # Step 2: "Spend" the characters for the ransomNote
        for char in ransomNote:
            if char not in counts or counts[char] <= 0:
                return False
            counts[char] -= 1
            
        return True