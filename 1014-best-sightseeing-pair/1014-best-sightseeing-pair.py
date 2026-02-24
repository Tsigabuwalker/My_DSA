class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_i = values[0] + 0
        result = 0
        for j in range(1, len(values)):
            result = max(result, max_i + values[j] - j)
            max_i = max(max_i, values[j] + j)
        return result