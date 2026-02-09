class Solution:
    def __init__(self, n, blacklist):
        self.size = n - len(blacklist)
        self.map = {}

        # mark blacklisted numbers
        black = {}
        for b in blacklist:
            black[b] = 1

        last = n - 1

        for b in blacklist:
            if b < self.size:
                while last in black:
                    last -= 1
                self.map[b] = last
                last -= 1

    def pick(self):
        # assume randint(a, b) exists
        x = randint(0, self.size - 1)
        if x in self.map:
            return self.map[x]
        return x
