class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        current_sum = sum(nums)
        diff = abs(goal - current_sum)
        
        # ceil(diff / limit)
        return (diff + limit - 1) // limit
