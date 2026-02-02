class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)  # Using a set for O(1) lookups
        memo = {}

        def backtrack(remaining):
            # If we've already solved this suffix, return the stored result
            if remaining in memo:
                return memo[remaining]
            
            # Base case: if the string is empty, return a list with an empty string
            if not remaining:
                return [""]
            
            res = []
            # Try every possible prefix of the remaining string
            for i in range(1, len(remaining) + 1):
                prefix = remaining[:i]
                if prefix in word_set:
                    # Recursively find sentences for the suffix
                    suffixes = backtrack(remaining[i:])
                    for suffix in suffixes:
                        # Combine prefix and suffix with a space
                        sentence = prefix + (" " + suffix if suffix else "")
                        res.append(sentence)
            
            memo[remaining] = res
            return res

        return backtrack(s)