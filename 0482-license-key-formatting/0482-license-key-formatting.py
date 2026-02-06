class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: Remove all dashes and convert to uppercase
        s = s.replace("-", "").upper()
        
        res = []
        # Step 2: Process the string from the end in chunks of size k
        while s:
            res.append(s[-k:])  # Take last k characters
            s = s[:-k]           # Remove last k characters
        
        # Step 3: Reverse the list and join with dashes
        return "-".join(res[::-1])
