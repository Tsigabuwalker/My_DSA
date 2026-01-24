class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev_s = s[::-1]
        new_s = s + "#" + rev_s

        # Build LPS array
        lps = [0] * len(new_s)
        for i in range(1, len(new_s)):
            j = lps[i-1]
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j-1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j

        # Characters after the longest palindromic prefix
        add = rev_s[:len(s)-lps[-1]]
        return add + s
