from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_rest = []
        guess_rest = []

        # First pass: count bulls
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_rest.append(s)
                guess_rest.append(g)

        # Second pass: count cows
        secret_count = Counter(secret_rest)
        cows = 0

        for g in guess_rest:
            if secret_count[g] > 0:
                cows += 1
                secret_count[g] -= 1

        return f"{bulls}A{cows}B"
