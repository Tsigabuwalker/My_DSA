class Solution:
    def minimumAbsDifference(self, arr):
        # Step 1: Sort the array
        arr.sort()
        min_diff = float('inf')
        
        # Step 2: Find the minimum absolute difference
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])
        
        # Step 3: Collect all pairs with the minimum difference
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])
        
        return result

# Example usage:
sol = Solution()
print(sol.minimumAbsDifference([4,2,1,3]))           # [[1,2],[2,3],[3,4]]
print(sol.minimumAbsDifference([1,3,6,10,15]))       # [[1,3]]
print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))  # [[-14,-10],[19,23],[23,27]]
