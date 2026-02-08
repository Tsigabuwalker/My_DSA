class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_candies = len(set(candyType))
        limit = len(candyType) // 2
        
        return min(unique_candies, limit)