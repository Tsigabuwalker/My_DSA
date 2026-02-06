class Solution:
    def removeInvalidParentheses(self, s: str):
        # Check if a string has valid parentheses
        def is_valid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        result = []
        visited = {}     # used like a set
        queue = [s]
        visited[s] = True
        found = False
        index = 0

        # BFS using list as queue
        while index < len(queue):
            curr = queue[index]
            index += 1

            if is_valid(curr):
                result.append(curr)
                found = True

            # If valid strings found at this level, stop deeper removals
            if found:
                continue

            for i in range(len(curr)):
                if curr[i] != '(' and curr[i] != ')':
                    continue

                next_str = curr[:i] + curr[i+1:]

                if next_str not in visited:
                    visited[next_str] = True
                    queue.append(next_str)

        return result
