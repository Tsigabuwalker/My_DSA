class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        memo = {}

        def can_win(used_mask, total):
            if used_mask in memo:
                return memo[used_mask]

            for i in range(maxChoosableInteger):
                if not (used_mask & (1 << i)):
                    if total + i + 1 >= desiredTotal:
                        memo[used_mask] = True
                        return True
                    
                    if not can_win(used_mask | (1 << i), total + i + 1):
                        memo[used_mask] = True
                        return True

            memo[used_mask] = False
            return False

        return can_win(0, 0)