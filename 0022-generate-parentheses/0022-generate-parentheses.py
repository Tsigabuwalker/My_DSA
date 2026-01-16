class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base Case: If the string has reached length 2 * n, it's complete
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Choice 1: Add an opening parenthesis
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # Choice 2: Add a closing parenthesis (only if it won't break balance)
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        # Start the recursion with an empty string
        backtrack("", 0, 0)
        return result