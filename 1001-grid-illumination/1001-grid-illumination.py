class Solution:
    def gridIllumination(self, n, lamps, queries):
        lamps_set = {}  # use dict to simulate a set
        row_count = {}
        col_count = {}
        diag_count = {}
        anti_diag_count = {}

        # Step 1: initialize counts
        for r, c in lamps:
            if (r, c) in lamps_set:
                continue
            lamps_set[(r, c)] = True
            row_count[r] = row_count.get(r, 0) + 1
            col_count[c] = col_count.get(c, 0) + 1
            diag_count[r - c] = diag_count.get(r - c, 0) + 1
            anti_diag_count[r + c] = anti_diag_count.get(r + c, 0) + 1

        ans = []

        # 8 directions including self
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),  (0,0),  (0,1),
                      (1,-1),  (1,0),  (1,1)]

        for r, c in queries:
            # Check if illuminated
            if (row_count.get(r, 0) > 0 or
                col_count.get(c, 0) > 0 or
                diag_count.get(r - c, 0) > 0 or
                anti_diag_count.get(r + c, 0) > 0):
                ans.append(1)
            else:
                ans.append(0)

            # Turn off lamp at (r,c) and neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in lamps_set:
                    del lamps_set[(nr, nc)]
                    row_count[nr] -= 1
                    if row_count[nr] == 0:
                        del row_count[nr]
                    col_count[nc] -= 1
                    if col_count[nc] == 0:
                        del col_count[nc]
                    diag_count[nr - nc] -= 1
                    if diag_count[nr - nc] == 0:
                        del diag_count[nr - nc]
                    anti_diag_count[nr + nc] -= 1
                    if anti_diag_count[nr + nc] == 0:
                        del anti_diag_count[nr + nc]

        return ans
