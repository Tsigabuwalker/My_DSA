class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1  # +1 or -1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1

            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1

            elif ch == '(':
                # Save current state
                stack.append(result)
                stack.append(sign)
                # Reset for new expression
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * num
                num = 0
                # Restore previous state
                result *= stack.pop()   # sign before '('
                result += stack.pop()   # result before '('

        # Add any remaining number
        result += sign * num
        return result
