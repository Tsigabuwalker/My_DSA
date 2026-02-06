class Solution:
    def addOperators(self, num: str, target: int):
        result = []

        def dfs(index, path, value, prev):
            # If we've used all digits
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i > index and num[index] == '0':
                    break

                curr_str = num[index:i+1]
                curr = int(curr_str)

                if index == 0:
                    # First number, no operator
                    dfs(i + 1, curr_str, curr, curr)
                else:
                    dfs(i + 1, path + "+" + curr_str, value + curr, curr)
                    dfs(i + 1, path + "-" + curr_str, value - curr, -curr)
                    # Handle multiplication
                    dfs(
                        i + 1,
                        path + "*" + curr_str,
                        value - prev + prev * curr,
                        prev * curr
                    )

        dfs(0, "", 0, 0)
        return result
