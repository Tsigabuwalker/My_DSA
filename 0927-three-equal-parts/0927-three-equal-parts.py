class Solution:
    def threeEqualParts(self, arr):
        n = len(arr)
        totalOnes = sum(arr)
        
        if totalOnes % 3 != 0:
            return [-1, -1]
        if totalOnes == 0:
            return [0, n-1]
        
        target = totalOnes // 3
        ones_positions = [i for i, bit in enumerate(arr) if bit == 1]
        
        first = ones_positions[0]
        second = ones_positions[target]
        third = ones_positions[2*target]
        
        length = n - third
        if arr[first:first+length] == arr[second:second+length] == arr[third:]:
            return [first+length-1, second+length]
        else:
            return [-1, -1]


# Example usage
sol = Solution()
print(sol.threeEqualParts([1,0,1,0,1]))   # Output: [0,3]
print(sol.threeEqualParts([1,1,0,1,1]))   # Output: [-1,-1]
print(sol.threeEqualParts([1,1,0,0,1]))   # Output: [0,2]
