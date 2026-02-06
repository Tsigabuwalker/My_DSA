class Solution:
    def maxProduct(self, words):
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        # Step 1: Convert each word to a bitmask
        for i in range(n):
            mask = 0
            for ch in words[i]:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask
            lengths[i] = len(words[i])

        max_prod = 0

        # Step 2: Compare all pairs
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:  # no common letters
                    prod = lengths[i] * lengths[j]
                    if prod > max_prod:
                        max_prod = prod

        return max_prod
