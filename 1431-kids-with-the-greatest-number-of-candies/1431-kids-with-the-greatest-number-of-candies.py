class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [(c + extraCandies) >= max_candies for c in candies]
