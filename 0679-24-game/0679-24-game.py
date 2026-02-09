class Solution:
    def judgePoint24(self, cards):
        EPS = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    next_nums = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    a, b = nums[i], nums[j]

                    # Try all operations
                    for val in (
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ):
                        next_nums.append(val)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

                    # Division (avoid division by zero)
                    if abs(b) > EPS:
                        next_nums.append(a / b)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

                    if abs(a) > EPS:
                        next_nums.append(b / a)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

            return False

        return dfs(list(map(float, cards)))
