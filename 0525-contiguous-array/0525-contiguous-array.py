from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        first_seen = {0: -1}
        max_len = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in first_seen:
                max_len = max(max_len, i - first_seen[count])
            else:
                first_seen[count] = i

        return max_len
