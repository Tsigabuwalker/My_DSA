class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(side):
            x_coef = 0
            const = 0
            i = 0
            sign = 1

            while i < len(side):
                if side[i] == '+':
                    sign = 1
                    i += 1
                elif side[i] == '-':
                    sign = -1
                    i += 1

                num = 0
                is_number = False
                while i < len(side) and side[i].isdigit():
                    num = num * 10 + int(side[i])
                    i += 1
                    is_number = True

                # ✅ FIXED LINE HERE
                if i < len(side) and side[i] == 'x':
                    x_coef += sign * (num if is_number else 1)
                    i += 1
                else:
                    const += sign * num

            return x_coef, const

        left, right = equation.split('=')
        lx, lc = parse(left)
        rx, rc = parse(right)

        coef = lx - rx
        const = rc - lc

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        return f"x={const // coef}"
