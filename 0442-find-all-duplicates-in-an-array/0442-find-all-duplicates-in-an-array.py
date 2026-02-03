class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        
        for x in nums:
            # Get the index this value "maps" to
            index = abs(x) - 1
            
            # If the number at that index is negative, we've seen it before
            if nums[index] < 0:
                result.append(abs(x))
            else:
                # Mark it as seen by making it negative
                nums[index] = -nums[index]
                
        return result