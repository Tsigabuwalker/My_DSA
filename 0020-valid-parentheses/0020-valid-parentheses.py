class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in bracket_map.values():  # opening brackets
                stack.append(char)
            else:  # closing brackets
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()

        return not stack  # True if stack is empty
