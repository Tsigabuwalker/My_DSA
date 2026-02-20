class Solution:
    def countOfAtoms(self, formula):
        stack = [{}]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1

            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i]) if start < i else 1

                top = stack.pop()
                for key in top:
                    top[key] *= mult
                    if key in stack[-1]:
                        stack[-1][key] += top[key]
                    else:
                        stack[-1][key] = top[key]

            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]

                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1

                if name in stack[-1]:
                    stack[-1][name] += count
                else:
                    stack[-1][name] = count

        result = ""
        final_map = stack[-1]

        for key in sorted(final_map):
            result += key
            if final_map[key] > 1:
                result += str(final_map[key])

        return result