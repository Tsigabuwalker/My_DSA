class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Step 1: Mark indices as "visited" by negating values
        for x in nums:
            index = abs(x) - 1
            # Only negate if it's currently positive
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Identify indices that were never visited
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # The index i corresponds to the number i + 1
                result.append(i + 1)
                
        return result