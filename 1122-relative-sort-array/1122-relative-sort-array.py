class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = [0] * 1001
        
        # Count frequency of each number in arr1
        for num in arr1:
            count[num] += 1
        
        result = []
        
        # Add numbers in the order of arr2
        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0
        
        # Add remaining numbers in ascending order
        for num in range(1001):
            if count[num] > 0:
                result.extend([num] * count[num])
        
        return result
