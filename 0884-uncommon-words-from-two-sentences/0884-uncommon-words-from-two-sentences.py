from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter((s1 + " " + s2).split())
        return [word for word, freq in count.items() if freq == 1]
