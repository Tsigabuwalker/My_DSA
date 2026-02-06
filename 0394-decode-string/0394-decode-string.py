class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_str = ''
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                num_stack.append(k)
                str_stack.append(current_str)
                current_str = ''
                k = 0
            elif ch == ']':
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat
            else:
                current_str += ch

        return current_str
