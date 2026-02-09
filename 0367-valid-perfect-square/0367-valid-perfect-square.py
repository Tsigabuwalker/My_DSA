class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        
        left = 1
        right = num
        
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
