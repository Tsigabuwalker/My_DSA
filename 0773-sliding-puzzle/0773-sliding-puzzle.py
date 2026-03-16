from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        # Flatten the board into a string for easy state comparison
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"

        # Neighbor positions for each index in the flattened string
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # BFS setup
        queue = deque([(start, start.index('0'), 0)])  # (state, zero_index, moves)
        visited = {start}

        while queue:
            state, zero, moves = queue.popleft()
            if state == target:
                return moves

            for nei in neighbors[zero]:
                new_state = list(state)
                # Swap zero with neighbor
                new_state[zero], new_state[nei] = new_state[nei], new_state[zero]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, nei, moves + 1))

        return -1
