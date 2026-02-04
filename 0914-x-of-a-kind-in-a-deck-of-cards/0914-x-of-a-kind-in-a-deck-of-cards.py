class Solution:
    def hasGroupsSizeX(self, deck):
        # Count frequencies
        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1

        # Compute GCD of counts
        freqs = list(count.values())

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = freqs[0]
        for f in freqs[1:]:
            g = gcd(g, f)

        return g >= 2
