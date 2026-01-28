class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n
        k = len(primes)

        # One pointer per prime
        idx = [0] * k

        for i in range(1, n):
            # Next possible ugly numbers
            next_vals = [primes[j] * ugly[idx[j]] for j in range(k)]
            next_ugly = min(next_vals)
            ugly[i] = next_ugly

            # Move all pointers that match next_ugly
            for j in range(k):
                if next_vals[j] == next_ugly:
                    idx[j] += 1

        return ugly[n - 1]
