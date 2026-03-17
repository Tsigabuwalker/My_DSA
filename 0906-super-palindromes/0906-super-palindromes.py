class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        ans = 0

        def is_palindrome(x: str) -> bool:
            return x == x[::-1]

        # Generate palindrome roots
        # Odd and even length palindromes
        for k in range(1, 100000):  # enough to cover sqrt(1e18)
            s = str(k)
            # Odd length palindrome
            pal = int(s + s[-2::-1])
            square = pal * pal
            if square > R:
                break
            if square >= L and is_palindrome(str(square)):
                ans += 1

            # Even length palindrome
            pal = int(s + s[::-1])
            square = pal * pal
            if square > R:
                continue
            if square >= L and is_palindrome(str(square)):
                ans += 1

        return ans


# Example usage:
sol = Solution()
print(sol.superpalindromesInRange("4", "1000"))   # Output: 4
print(sol.superpalindromesInRange("1", "2"))      # Output: 1
