class Solution:
    def numRabbits(self, answers):
        count_map = {}
        for ans in answers:
            if ans in count_map:
                count_map[ans] += 1
            else:
                count_map[ans] = 1
        
        total = 0
        for ans, count in count_map.items():
            group_size = ans + 1
            # Number of groups needed for this answer
            groups = (count + group_size - 1) // group_size  # ceil division
            total += groups * group_size
        
        return total
