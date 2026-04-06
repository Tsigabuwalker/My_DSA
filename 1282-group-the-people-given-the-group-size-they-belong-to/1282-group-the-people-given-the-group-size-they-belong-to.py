class Solution:
    def groupThePeople(self, groupSizes):
        size_map = {}   # size → list of people
        result = []
        
        for i, size in enumerate(groupSizes):
            if size not in size_map:
                size_map[size] = []
            
            size_map[size].append(i)
            
            # If group is full, add to result
            if len(size_map[size]) == size:
                result.append(size_map[size])
                size_map[size] = []
        
        return result