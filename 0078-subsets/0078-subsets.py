class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start, current_subset):
            # Every step in our recursion is a valid subset, 
            # so we add a copy to our results.
            res.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # 1. Include the number
                current_subset.append(nums[i])
                
                # 2. Move to the next element
                backtrack(i + 1, current_subset)
                
                # 3. Backtrack (remove the number) to explore other paths
                current_subset.pop()
                
        backtrack(0, [])
        return res