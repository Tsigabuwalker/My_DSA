class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        # sort in ascending order
        satisfaction.sort()
        
        total = 0
        curr = 0
        
        # start from the largest satisfaction
        for s in reversed(satisfaction):
            if curr + s > 0:
                curr += s
                total += curr
            else:
                break
        
        return total
