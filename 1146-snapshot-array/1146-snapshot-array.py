class SnapshotArray:
    def __init__(self, length):
        # For each index, store a list of (snap_id, value) pairs
        self.data = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        # If the last entry for this index has the same snap_id, update it
        if self.data[index] and self.data[index][-1][0] == self.snap_id:
            self.data[index][-1][1] = val
        else:
            # Otherwise, append a new record
            self.data[index].append([self.snap_id, val])

    def snap(self):
        # Return current snap_id, then increment
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        # Binary search manually (since no imports allowed)
        arr = self.data[index]
        left, right = 0, len(arr) - 1
        res = 0  # default value if no entry found
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
