class Solution:
    def minCost(self, colors, neededTime):
        total_time = 0
        n = len(colors)
        i = 0
        
        while i < n:
            # Start of a consecutive group
            j = i
            max_time = neededTime[i]
            sum_time = neededTime[i]
            
            # Count the group of same colors
            while j + 1 < n and colors[j + 1] == colors[i]:
                j += 1
                sum_time += neededTime[j]
                max_time = max(max_time, neededTime[j])
            
            # Remove all except the one with max_time
            total_time += sum_time - max_time
            
            # Move to the next group
            i = j + 1
        
        return total_time

# Example usage:
sol = Solution()
print(sol.minCost("abaac", [1,2,3,4,5]))  # Output: 3
print(sol.minCost("abc", [1,2,3]))        # Output: 0
print(sol.minCost("aabaa", [1,2,3,4,1]))  # Output: 2
