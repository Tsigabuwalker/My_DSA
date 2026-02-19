class Solution:
    def minCost(self, nums, cost):
        pairs = sorted(zip(nums, cost))
        
        total_weight = sum(cost)
        cumulative = 0
        
        # Find weighted median
        median = 0
        for num, c in pairs:
            cumulative += c
            if cumulative >= total_weight / 2:
                median = num
                break
        
        # Calculate total cost
        result = 0
        for num, c in pairs:
            result += abs(num - median) * c
        
        return result
