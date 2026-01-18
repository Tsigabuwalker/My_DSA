class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to serve as a base for length calculation
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the opening bracket
                stack.append(i)
            else:
                # We encountered a ')', so pop the last starting point
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' is a new starting boundary
                    stack.append(i)
                else:
                    # Calculate the distance between current index and the new top
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
                    
        return max_length