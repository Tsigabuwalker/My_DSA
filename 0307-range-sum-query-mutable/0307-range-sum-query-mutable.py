class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]  # copy of original array
        self.tree = [0] * (self.n + 1)

        # Build Fenwick Tree
        for i in range(self.n):
            self._update_tree(i + 1, nums[i])

    def _update_tree(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def _query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self._update_tree(index + 1, delta)

    def sumRange(self, left, right):
        return self._query(right + 1) - self._query(left)