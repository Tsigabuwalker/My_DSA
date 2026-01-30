class Solution:
    def diffWaysToCompute(self, expression: str):
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    for l in left_results:
                        for r in right_results:
                            if ch == '+':
                                results.append(l + r)
                            elif ch == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)

            # Base case: expr is a number
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return compute(expression)
