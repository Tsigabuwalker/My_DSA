class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to handle duplicates
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])  # i+1 because each number used once
                path.pop()

        backtrack(0, [], target)
        return result
