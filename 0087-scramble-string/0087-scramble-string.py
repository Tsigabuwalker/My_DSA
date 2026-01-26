class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dfs(a, b):
            # If already computed
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Base case: strings are equal
            if a == b:
                memo[(a, b)] = True
                return True
            
            # Base case: if lengths differ or character counts differ
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            
            n = len(a)
            # Try all split positions
            for i in range(1, n):
                # Case 1: no swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Case 2: swap
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False

        return dfs(s1, s2)
