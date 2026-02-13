class Solution:
    def getMaxLen(self, nums):
        # pos: length of subarray ending here with positive product
        # neg: length of subarray ending here with negative product
        pos = 0
        neg = 0
        max_len = 0
        
        for num in nums:
            if num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif num < 0:
                temp = pos
                pos = neg + 1 if neg > 0 else 0
                neg = temp + 1
            else:
                pos = 0
                neg = 0
            max_len = max(max_len, pos)
        
        return max_len

# Example usage:
sol = Solution()
print(sol.getMaxLen([1,-2,-3,4]))          # Output: 4
print(sol.getMaxLen([0,1,-2,-3,-4]))       # Output: 3
print(sol.getMaxLen([-1,-2,-3,0,1]))       # Output: 2
