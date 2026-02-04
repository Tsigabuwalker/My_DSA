class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = 0
        sumB = 0

        for a in aliceSizes:
            sumA += a
        for b in bobSizes:
            sumB += b

        diff = (sumB - sumA) // 2

        bobSet = {}
        for b in bobSizes:
            bobSet[b] = True

        for a in aliceSizes:
            if a + diff in bobSet:
                return [a, a + diff]
