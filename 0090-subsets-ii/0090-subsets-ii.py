class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # sort to handle duplicates
        res = []

        def backtrack(start, path):
            res.append(path[:])  # add current subset
            
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()  # backtrack
        
        backtrack(0, [])
        return res
