class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Base Case: If the string is too short, no substring can satisfy k
        if len(s) < k:
            return 0
        
        # Count the frequency of each character in the current string
        # Using a simple dictionary or Counter
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        # Check every character to see if it acts as a "splitter"
        for char, freq in counts.items():
            if freq < k:
                # This char cannot be in our result. 
                # Split s by this character and check the resulting parts.
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # If we reach here, it means all characters in s meet the frequency k
        return len(s)