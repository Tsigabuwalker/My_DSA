class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # Helper: compute f(x)
        def f(x: int) -> int:
            res = 0
            while x > 0:
                res += x // 5
                x //= 5
            return res

        # Binary search to see if there exists an x with f(x) == k
        left, right = 0, 5 * k
        while left <= right:
            mid = (left + right) // 2
            val = f(mid)
            if val == k:
                return 5   # Always 5 consecutive solutions
            elif val < k:
                left = mid + 1
            else:
                right = mid - 1
        return 0
