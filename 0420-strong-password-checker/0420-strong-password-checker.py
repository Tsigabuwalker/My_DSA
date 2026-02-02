class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        n = len(s)
        missing_lower = 1
        missing_upper = 1
        missing_digit = 1

        for c in s:
            if c.islower():
                missing_lower = 0
            elif c.isupper():
                missing_upper = 0
            elif c.isdigit():
                missing_digit = 0

        missing_types = missing_lower + missing_upper + missing_digit

        # Find repeating sequences
        i = 2
        repeats = []
        while i < n:
            if s[i] == s[i-1] == s[i-2]:
                length = 2
                while i < n and s[i] == s[i-1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        if n < 6:
            # Need insertions to reach length 6
            return max(6 - n, missing_types)
        else:
            # Number of deletions if password too long
            over_len = max(n - 20, 0)
            left_over = 0  # replacements needed for remaining repeats
            repeats.sort()
            deletions = over_len

            # Greedy: remove 1,2,3... from repeats to reduce replacements
            for i in range(len(repeats)):
                if deletions > 0 and repeats[i] >= 3:
                    remove = min(repeats[i] - 2, deletions)
                    repeats[i] -= remove
                    deletions -= remove

            # After deletions, count replacements for remaining repeats
            replacements = sum(r // 3 for r in repeats)

            if n <= 20:
                return max(missing_types, replacements)
            else:
                return over_len + max(missing_types, replacements)
