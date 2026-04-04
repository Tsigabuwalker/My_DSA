class Solution:
    def isIdealPermutation(self, nums):
        """
        Check if the number of global inversions equals the number of local inversions.
        
        :param nums: List[int] - a permutation of [0, n-1]
        :return: bool
        """
        for i, num in enumerate(nums):
            
            if abs(num - i) > 1:
                return False
        return True

sol = Solution()
print(sol.isIdealPermutation([1, 0, 2]))  # Output: True
print(sol.isIdealPermutation([1, 2, 0]))  # Output: False
