class Solution:
    def primePalindrome(self, n: int) -> int:
        # Step 1: small direct cases
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if 8 <= n <= 11:
            return 11

        # Step 2: generate odd-length palindromes
        # Only odd-length palindromes needed (even-length > 11 divisible by 11)
        length = 1
        while True:
            start = 10**(length - 1)
            end = 10**length
            for first_half in range(start, end):
                s = str(first_half)
                palindrome = int(s + s[-2::-1])  # odd-length palindrome
                if palindrome >= n and self.isPrime(palindrome):
                    return palindrome
            length += 1

    def isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True
