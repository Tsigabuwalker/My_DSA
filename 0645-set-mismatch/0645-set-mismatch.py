class Solution:
    def findErrorNums(self, nums):
        seen = set()
        duplicate = -1
        
        # Find duplicate
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        # Find missing
        n = len(nums)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
        
        return [duplicate, missing]