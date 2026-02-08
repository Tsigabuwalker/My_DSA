class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = {}
        for j in jewels:
            jewel_set[j] = True

        count = 0
        for s in stones:
            if s in jewel_set:
                count += 1

        return count
