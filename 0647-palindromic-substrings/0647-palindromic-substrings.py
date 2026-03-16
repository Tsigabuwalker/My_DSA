class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expandAroundCenter(left: int, right: int) -> int:
            local_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count

        for i in range(n):
            # Odd-length palindromes centered at i
            count += expandAroundCenter(i, i)
            # Even-length palindromes centered between i and i+1
            count += expandAroundCenter(i, i + 1)

        return count


# Example usage:
sol = Solution()
print(sol.countSubstrings("abc"))  # Output: 3
print(sol.countSubstrings("aaa"))  # Output: 6
