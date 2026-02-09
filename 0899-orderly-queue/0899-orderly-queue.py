class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # Generate all rotations and pick the smallest
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            # Any permutation possible
            return ''.join(sorted(s))
