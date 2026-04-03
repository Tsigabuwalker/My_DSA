class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        seen = set()
        
        for value in count.values():
            if value in seen:
                return False
            seen.add(value)
        
        return True