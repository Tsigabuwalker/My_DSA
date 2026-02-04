class Solution:
    def numSpecialEquivGroups(self, words):
        groups = {}

        for word in words:
            even_chars = []
            odd_chars = []
            for i, c in enumerate(word):
                if i % 2 == 0:
                    even_chars.append(c)
                else:
                    odd_chars.append(c)
            # Sort to get canonical form
            key = ''.join(sorted(even_chars)) + ''.join(sorted(odd_chars))
            groups[key] = True

        return len(groups)
