class WordFilter:
    def __init__(self, words):
        self.lookup = {}
        for index, word in enumerate(words):
            length = len(word)
            # Generate all prefix and suffix combinations
            for i in range(length + 1):
                prefix = word[:i]
                for j in range(length + 1):
                    suffix = word[j:]
                    key = suffix + "#" + prefix
                    self.lookup[key] = index

    def f(self, pref, suff):
        key = suff + "#" + pref
        return self.lookup.get(key, -1)