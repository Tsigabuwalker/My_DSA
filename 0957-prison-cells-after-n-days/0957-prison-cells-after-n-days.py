class Solution:
    def prisonAfterNDays(self, cells, n):
        seen = {}
        is_cycle = False

        while n > 0:
            # Convert current state to tuple for hashing
            state_key = tuple(cells)
            if state_key in seen:
                # Cycle detected
                cycle_length = seen[state_key] - n
                n %= cycle_length
                is_cycle = True
                if n == 0:
                    break
            else:
                seen[state_key] = n

            if n > 0:
                n -= 1
                cells = self.nextDay(cells)

        return cells

    def nextDay(self, cells):
        new_cells = [0]  # first cell always becomes 0
        for i in range(1, len(cells) - 1):
            new_cells.append(1 if cells[i-1] == cells[i+1] else 0)
        new_cells.append(0)  # last cell always becomes 0
        return new_cells
