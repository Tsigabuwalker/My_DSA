class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        candidates = {}

        def make_pal(prefix, odd):
            if odd:
                return prefix + prefix[:-1][::-1]
            else:
                return prefix + prefix[::-1]

        half_len = (length + 1) // 2
        prefix = int(n[:half_len])

        for x in (prefix - 1, prefix, prefix + 1):
            if x >= 0:
                p = make_pal(str(x), length % 2 == 1)
                candidates[int(p)] = True

        candidates[10 ** (length - 1) - 1] = True
        candidates[10 ** length + 1] = True

        best = -1
        best_diff = -1

        for cand in candidates:
            if cand == num:
                continue
            diff = abs(cand - num)
            if best == -1 or diff < best_diff or (diff == best_diff and cand < best):
                best = cand
                best_diff = diff

        return str(best)
