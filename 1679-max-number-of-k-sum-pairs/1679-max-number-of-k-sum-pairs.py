from collections import defaultdict

class Solution:
    def maxOperations(self, nums, k):
        count = defaultdict(int)
        operations = 0

        for num in nums:
            complement = k - num
            if count[complement] > 0:
                count[complement] -= 1
                operations += 1
            else:
                count[num] += 1

        return operations
