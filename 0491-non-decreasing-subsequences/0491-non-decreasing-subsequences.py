class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start, path):
            if len(path) >= 2:
                res.append(list(path))
            
            used_in_level = set()
            for i in range(start, len(nums)):
                if nums[i] in used_in_level:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    used_in_level.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
                    
        backtrack(0, [])
        return res