class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            needed = mid * (mid + 1) // 2
            
            if needed == n:
                return mid
            elif needed < n:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
