class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # pair lightest
            right -= 1     # heaviest always boards
            boats += 1
        
        return boats
