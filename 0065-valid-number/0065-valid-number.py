class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch in ['+', '-']:
                # Sign must be at start or just after exponent
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                # Dot can't appear after exponent or twice
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in ['e', 'E']:
                # Exponent must follow a digit and appear once
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # reset for exponent digits

            else:
                return False

        return seen_digit
