class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]

class Solution:
    def prime_factors(self, x):
        factors = set()
        while x % 2 == 0:
            factors.add(2)
            x //= 2
        f = 3
        while f * f <= x:
            while x % f == 0:
                factors.add(f)
                x //= f
            f += 2
        if x > 1:
            factors.add(x)
        return factors

    def largestComponentSize(self, nums: list[int]) -> int:
        n = len(nums)
        dsu = DSU(n)
        factor_to_index = {}

        for i in range(n):
            num = nums[i]
            for factor in self.prime_factors(num):
                if factor in factor_to_index:
                    dsu.union(i, factor_to_index[factor])
                factor_to_index[factor] = i

        count = {}
        max_size = 0
        for i in range(n):
            parent = dsu.find(i)
            if parent not in count:
                count[parent] = 0
            count[parent] += 1
            if count[parent] > max_size:
                max_size = count[parent]

        return max_size
