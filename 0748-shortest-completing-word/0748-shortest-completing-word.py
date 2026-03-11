from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words):
        # Extract letters and count frequency
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        result = None

        for word in words:
            word_count = Counter(word)

            # Check if word satisfies the requirement
            if all(word_count[c] >= required[c] for c in required):
                if result is None or len(word) < len(result):
                    result = word

        return result