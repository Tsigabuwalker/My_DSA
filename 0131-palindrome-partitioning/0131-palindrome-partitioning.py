class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(start: int, path: list[str]):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:  # check palindrome
                    path.append(substring)
                    backtrack(end+1, path)
                    path.pop()  # backtrack
        
        backtrack(0, [])
        return res
