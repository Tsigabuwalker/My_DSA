class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize result array with zeros
        ans = [0] * (n + 1)
        
        # Fill the array using the recurrence relation
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans


# Example usage:
sol = Solution()
print(sol.countBits(2))  # Output: [0, 1, 1]
print(sol.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
