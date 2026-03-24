class Solution:
    def dominantIndex(self, nums):
        max1 = -1
        max2 = -1
        index = -1
        
        for i, num in enumerate(nums):
            if num > max1:
                max2 = max1
                max1 = num
                index = i
            elif num > max2:
                max2 = num
        
        return index if max1 >= 2 * max2 else -1