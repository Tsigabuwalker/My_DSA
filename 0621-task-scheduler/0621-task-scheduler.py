from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxFreq)
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)

