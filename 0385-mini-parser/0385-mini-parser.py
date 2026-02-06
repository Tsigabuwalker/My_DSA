class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = ''
        negative = False
        
        for ch in s:
            if ch == '-':
                negative = True
            elif ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(NestedInteger())
            elif ch == ',' or ch == ']':
                if num:
                    value = int(num) if not negative else -int(num)
                    stack[-1].add(NestedInteger(value))
                    num = ''
                    negative = False
                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
        
        return stack[0]
