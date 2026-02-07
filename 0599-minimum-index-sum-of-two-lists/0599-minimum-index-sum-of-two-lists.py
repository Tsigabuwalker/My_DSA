class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}
        for i, s in enumerate(list1):
            index_map[s] = i
        
        min_sum = float('inf')
        result = []
        
        for j, s in enumerate(list2):
            if s in index_map:
                curr_sum = index_map[s] + j
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [s]
                elif curr_sum == min_sum:
                    result.append(s)
        
        return result
