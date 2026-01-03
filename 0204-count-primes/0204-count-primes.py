class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        i = 2
        while i * i < n:
            if primes[i]:
                # mark multiples of i as non-prime
                for temp in range(i * i, n, i):
                    primes[temp] = False
            i += 1

        return sum(primes)
