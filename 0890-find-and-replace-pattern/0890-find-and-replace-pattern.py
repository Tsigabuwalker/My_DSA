class Solution:
    def findAndReplacePattern(self, words, pattern):
        res = []

        for word in words:
            if len(word) != len(pattern):
                continue

            p2w = {}
            w2p = {}
            match = True

            for pc, wc in zip(pattern, word):
                if pc in p2w:
                    if p2w[pc] != wc:
                        match = False
                        break
                else:
                    p2w[pc] = wc

                if wc in w2p:
                    if w2p[wc] != pc:
                        match = False
                        break
                else:
                    w2p[wc] = pc

            if match:
                res.append(word)

        return res
